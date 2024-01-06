# Queries over Structured Data (Pandas DataFrame / SQL Database)

# Setup: Define Example SQL Table
# Build Table Index: SQL Database -> Table Schema Index
# Natural Language SQL Queries: How to Query SQL Database using Natural Lanugage

# Setup w/ SQLAlchemy

from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    select,
    column,
)

engine = create_engine("sqlite:///:memory:")
metadata_obj = MetaData()

# Create a toy "city_stats" table
table_name = "city_stats"
city_stats_table = Table(
    table_name,
    metadata_obj,
    Column("city_name", String(16), primary_key = True),
    Column("population", Integer),
    Column("country", String(16), nullable = False),
)
metadata_obj.create_all(engine)

# Insert Datapoints
from sqlalchemy import insert
rows = [
    {"city_name": "Toronto", "population": 2731571, "country": "Canada"},
    {"city_name": "Tokyo", "population": 13929286, "country": "Japan"},
    {"city_name": "Berlin", "population": 600000, "country": ""}
]

for row in rows:
    stmt = insert(city_stats_table).values(**row)
    with engine.begin() as connection:
        cursor = connection.execute(stmt)

# Wrap SQLAlchemy Engine w/ SQLDatabase Wrapper --> Allows DB to be used in Llamaindex
from llama_index import SQLDatabase
sql_database = SQLDatabase(engine, include_tables = ["city_stats"])

# Natural Language SQL
from llama_index.indices.struct_store import NLSQLTableQueryEngine

# Specify Tables into Query Engine OR place all into Schema Context --> Overflow LLM Context Window
query_engine = NLSQLTableQueryEngine(
    sql_database = sql_database,
    tables = ["city_stats"],
)

query_str = "Which city has the highest population?"
response = query_engine.query(query_str)

# Building Table Index
from llama_index import VectorStoreIndex
from llama_index.objects import (
    SQLTableNodeMapping,
    ObjectIndex,
    SQLTableSchema,
)

table_node_mapping = SQLTableNodeMapping(sql_database)
table_schema_objs = [
    (SQLTableSchema(table_name="city_stats")),
] # One SQLTableSchema for Each Table

obj_index = ObjectIndex.from_objects(
    table_schema_objs,
    table_node_mapping,
    VectorStoreIndex, # VectorStoreIndex: Each Node has a Table Schema & Other Context Information 
)

# Manually Set Extra Context Text
city_stats_text = (
    "This table gives information regarding the population and country of a given city.\n"
    "The user will query with codewords, where 'foo' corresponds to population and 'bar'"
    "corresponds to city."
)

table_node_mapping = SQLDatabase(sql_database) # Refresh with new Database
table_schema_objs = [
    (SQLTableSchema(table_name = "city_stats", context_str = city_stats_text))
]

# Using Natural Language SQL Queries
from llama_index.indices.struct_store import SQLTableRetrieverQueryEngine

query_engine = SQLTableRetrieverQueryEngine(
    sql_database, obj_index.as_retriever(similarity_top_k = 1)
)

response = query_engine.query("Which city has the highest population?")
print(response)