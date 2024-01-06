import os.path

from llama_index import (
    VectorStoreIndex, 
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage, 
)

# Check if Storage Exists
if not os.path.exists("./storage"):
    # Load the Documents and Create the INdex
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    # Store it for later
    index.storage_context.persist()
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)

# either way we can now query the index
    
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)