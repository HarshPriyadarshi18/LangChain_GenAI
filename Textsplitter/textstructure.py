from langchain.text_splitter import RecursiveCharacterTextSplitter
text="""✅ Step 2: Each edge processed once (or twice)
for (auto nei : adj[node])
Every edge is checked when exploring adjacency list
In undirected graph:
edge (u, v) appears in both u and v list
so processed 2 times max

👉 Total edge work = O(E)

🔥 Final Complexity
Time = O(V) + O(E) = O(V + E)
🔹 Intuition (VERY IMPORTANT)

Imagine:

You walk through graph
You never revisit a node again
You only look at each edge while standing at a node

👉 So total work = nodes + edges"""
splitter=RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0
)
chunk=splitter.split_text(text)
print(chunk[0])

