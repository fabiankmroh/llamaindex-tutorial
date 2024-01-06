# Parsing Documents into Smaller Chunks
from llama_index import ServiceContext
from llama_index import VectorStoreIndex, SimpleDirectoryReader

service_context = ServiceContext.from_defaults(chunk_size = 1000)
documents = SimpleDirectoryReader("data").load_data()

# ServiceContext: Bundle of Services & Configurations across LlamadIndex Pipeline
index = VectorStoreIndex.from_documents( # Customization Line
    documents, service_context = service_context
)
query_engine = index.as_query_engine()

response = query_engine.query("What did the author do growing up?")
print(response)


# Using a Different Vector Store
import chromadb
from llama_index.vector_stores import ChromaVectorStore
from llama_index import StorageContext

chroma_client = chromadb.PersistentClient()
chroma_collection = chroma_client.create_collection("quickstart")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# StorageContext: Defines Storage Backend for Documents, Embeddings, Index Storage
from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents( # Customization Line
    documents, storage_context=storage_context
)
query_engine = index.as_query_engine()

response = query_engine.query("What did the author do growing up?")
print(response)


# Retrieve More Context for Query
from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents) 
query_engine = index.as_query_engine(similarity_top_k=5) # Customization Line

response = query_engine.query("What did the author do growing up?")
print(response)


# Different LLM
from llama_index import ServiceContext
from llama_index.llms import PaLM

service_context = ServiceContext.from_defaults(llm=PaLM())
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine(service_context=service_context) # Customization Line
response = query_engine.query("What did the author do growing up?")
print(response)

# Different Response Mode
from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine(response_mode = "tree_summarize")
response = query_engine.query("What did the author do growing up?")
print(response)


# Stream Response Back
from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine(response_mode="tree_summarize") # Customization Line
response = query_engine.query("What did the author do growing up?")
print(response)

# Chatbox instead of Q & A
from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_chat_engine() # Customization Line
response = query_engine.chat("What did the author do growing up?") # Customization Line
print(response)

response = query_engine.chat("Oh interesting, tell me more.") # Customization Line
print(response)