# Support More General Multi-Document Queries 
# Some Question 
from llama_index.tools import QueryEngineTool, ToolMetadata

query_engine_tools = [
    QueryEngineTool(
        query_engine = sept_engine,
        metadata = ToolMetadata(
            name = "sept_22",
            description = "Provides information about Uber quarterly financials ending September 2022",
        ),
    ),
    QueryEngineTool(
        query_engine = june_engine,
        metadata = ToolMetadata(
            name = "june_22",
            description = "Provides information about Uber quarterly financials ending June 2022",
        ),
    ), 
    QueryEngineTool(
        query_engine = march_engine,
        metadata = ToolMetadata(
            name = "march_22",
            description = "Provides information about Uber quarterly financials ending March 2022",
        ),
    ),
]

# Define SubQuestionQueryEngine over Tools
from llama_index.query_engine import SubQuestionQueryEngine

# Execute any Number of Sub-Queries (SQL in Another SQL) before Final Answer Synthesis
query_engine = SubQuestionQueryEngine.from_defaults(
    query_engine_tools = query_engine_tools
)
