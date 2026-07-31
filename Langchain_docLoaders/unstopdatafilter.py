import csv
import json
from pathlib import Path


INPUT_CSV = Path(__file__).with_name("unstop_output") / "unstop_leaderboard_rows.csv"
OUTPUT_DIR = Path(__file__).with_name("unstop_output")
OUTPUT_DIR.mkdir(exist_ok=True)


def is_nit_patna(row):
    haystack = " ".join(
        [row.get("team_name", ""), row.get("name", ""), row.get("organization", ""), row.get("raw_details", "")]
    ).lower()
    return "national institute of technology (nit), patna" in haystack or "nit, patna" in haystack


def main():
    if not INPUT_CSV.exists():
        raise FileNotFoundError(f"Missing input CSV: {INPUT_CSV}")

    filtered_rows = []

    with INPUT_CSV.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if is_nit_patna(row):
                filtered_rows.append(row)

    csv_path = OUTPUT_DIR / "unstop_nit_patna.csv"
    json_path = OUTPUT_DIR / "unstop_nit_patna.json"

    with csv_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["page", "team_name", "name", "organization", "players", "raw_details"])
        writer.writeheader()
        writer.writerows(filtered_rows)

    with json_path.open("w", encoding="utf-8") as file:
        json.dump(filtered_rows, file, ensure_ascii=False, indent=2)

    print(f"Filtered rows: {len(filtered_rows)}")
    print(f"Saved CSV to {csv_path}")
    print(f"Saved JSON to {json_path}")


if __name__ == "__main__":
    main()