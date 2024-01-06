# LlamaIndex supports Routing > Heterogeneous Data Sources
# RouterQueryEngine: Selects 1/7 Candidate Query Engines for Execution

# Build Sub-Indices over Different Data Sources 
from llama_index import TreeIndex, VectorStoreIndex
from llama_index.tools import QueryEngineTool

# Define Sub-Indices
index1 = VectorStoreIndex.from_documents(notion_docs)
index2 = VectorStoreIndex.from_documents(slack_docs)

# Define Query Engines & Tools
tool1 = QueryEngineTool.from_defaults(
    query_engine = index1.as_query_engine(),
    description = "Use this query engine to do...",
)

tool2 = QueryEngineTool.from_defaults(
    query_engine = index2.as_query_engine(),
    description = "Use this query engine for something else...",
)

# Define RouterQueryEngine --> Use LLMSingleSelector as Router (LLM choosing Best Sub-Index to Router the Query)
from llama_index.query_engine import RouterQueryEngine

query_engine = RouterQueryEngine.from_defaults(
    query_engine_tools = [tool1, tool2]
)

response = query_engine.query(
    "In Notion, give me a summary of the product roadmap."
)