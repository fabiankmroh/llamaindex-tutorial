# Combine Multiple Sources Over Documents: LlamaIndex can pull in Unstructured Text, PDFs --> Index Data in them

from llama_index import VectorStoreIndex, SummaryIndex
from llama_index.indices.composability import ComposableGraph

index1 = VectorStoreIndex.from_documents(notion_docs)
index2 = VectorStoreIndex.from_documents(slack_docs)

graph = ComposableGraph.from_indices(
    SummaryIndex, [index1, index2], index_summaries=["summary1", "summary2"]
)

query_engine = graph.as_query_engine()
response = query_engine.query("<query_str>")