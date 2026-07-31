import csv
import json
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


URL = "https://unstop.com/hackathons/crp-hackon-with-amazon-60-amazon-1682652/online-assessment/423480"
PAGE_COUNT = 10
OUTPUT_DIR = Path(__file__).with_name("unstop_output")
OUTPUT_DIR.mkdir(exist_ok=True)


def build_driver():
    user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    )

    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(f"--user-agent={user_agent}")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd(
        "Network.setUserAgentOverride",
        {"userAgent": user_agent, "platform": "Windows"},
    )
    driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});"},
    )
    return driver


def wait_for_table(driver):
    WebDriverWait(driver, 30).until(
        lambda browser: "Cookies Disabled" not in browser.page_source
        and "Please Wait" not in browser.page_source
        and len(browser.find_elements(By.CSS_SELECTOR, "table tbody tr")) > 0
    )


def normalize_text(value):
    return " ".join(value.split())


def parse_rows(driver):
    rows = []
    table_rows = driver.execute_script(
        """
        return Array.from(document.querySelectorAll('table tbody tr')).map((row) =>
          Array.from(row.querySelectorAll('td')).map((cell) => cell.innerText.trim())
        );
        """
    )

    for row in table_rows:
        if len(row) < 2:
            continue

        team_name = normalize_text(row[0])
        details = normalize_text(row[1])

        player_count = ""
        if "+" in details and "Player(s)" in details:
            details_parts = details.rsplit("+", 1)
            details = normalize_text(details_parts[0])
            player_count = "+" + details_parts[1]

        name = details
        organization = ""
        if "  " in details:
            name, organization = [normalize_text(part) for part in details.split("  ", 1)]

        rows.append(
            {
                "team_name": team_name,
                "name": name,
                "organization": organization,
                "players": player_count,
                "raw_details": details,
            }
        )

    return rows


def get_first_team_name(driver):
    return normalize_text(
        driver.execute_script(
            """
            const firstRow = document.querySelector('table tbody tr');
            const firstCell = firstRow ? firstRow.querySelector('td') : null;
            return firstCell ? firstCell.innerText : '';
            """
        )
    )


def click_page(driver, page_number):
    page_locator = (
        By.XPATH,
        f'//span[contains(@class, "number") and normalize-space()="{page_number}"]',
    )
    element = driver.find_element(*page_locator)
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'}); arguments[0].click();",
        element,
    )


def dismiss_overlays(driver):
    driver.execute_script(
        """
        for (const selector of ['#chrome_desktop_backend', '[id^="chrome_desktop_"]']) {
          document.querySelectorAll(selector).forEach((element) => element.remove());
        }
        """
    )


def main():
    driver = build_driver()
    all_pages = []

    try:
        driver.get(URL)
        wait_for_table(driver)
        dismiss_overlays(driver)

        for page_number in range(1, PAGE_COUNT + 1):
            wait_for_table(driver)
            page_rows = parse_rows(driver)

            if not page_rows:
                raise RuntimeError(f"No rows found on page {page_number}")

            current_first_team = page_rows[0]["team_name"]
            all_pages.append(
                {
                    "page": page_number,
                    "rows": page_rows,
                }
            )

            print(f"Page {page_number}: {len(page_rows)} rows, first team = {current_first_team}")

            if page_number < PAGE_COUNT:
                expected_first_team = current_first_team
                dismiss_overlays(driver)
                click_page(driver, page_number + 1)
                WebDriverWait(driver, 30).until(
                    lambda browser: get_first_team_name(browser) != expected_first_team
                )

        json_path = OUTPUT_DIR / "unstop_leaderboard_pages.json"
        csv_path = OUTPUT_DIR / "unstop_leaderboard_rows.csv"

        with json_path.open("w", encoding="utf-8") as file:
            json.dump(all_pages, file, ensure_ascii=False, indent=2)

        with csv_path.open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["page", "team_name", "name", "organization", "players", "raw_details"],
            )
            writer.writeheader()
            for page_data in all_pages:
                for row in page_data["rows"]:
                    writer.writerow({"page": page_data["page"], **row})

        print(f"Saved JSON to {json_path}")
        print(f"Saved CSV to {csv_path}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()