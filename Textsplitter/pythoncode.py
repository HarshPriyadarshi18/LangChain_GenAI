from langchain.text_splitter import RecursiveCharacterTextSplitter,Language
text="""bool dfs(int node, int col, vector<vector<int>>& adj, vector<int>& color) {
    color[node] = col;

    for (auto nei : adj[node]) {
        // If not colored → assign opposite color
        if (color[nei] == -1) {
            if (!dfs(nei, 1 - col, adj, color)) {
                return false;
            }
        }
        // If same color → conflict
        else if (color[nei] == col) {
            return false;
        }
    }
    return true;
}

bool isBipartite(int n, vector<vector<int>>& adj) {
    vector<int> color(n, -1);

    for (int i = 0; i < n; i++) {
        if (color[i] == -1) {
            if (!dfs(i, 0, adj, color)) {
                return false;
            }
        }
    }
    return true;
}"""
splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.CPP,
    chunk_size=200,
    chunk_overlap=0
)
chunk=splitter.split_text(text)
print(chunk[0])

