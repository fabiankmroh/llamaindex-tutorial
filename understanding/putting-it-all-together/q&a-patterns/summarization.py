# Summarization: Large Amount of Data --> Short Summary relevant to Current Question
from llama_index import SummaryIndex

index = SummaryIndex.from_documents(documents)

query_engine = index.as_query_engine(response_mode="tree summarize")
response = query_engine.query("<summarization_query")