
from chromadb import Client

# add ~/ottomator-agents/mem0-agent/iterations/python_tools/chroma_db_manager$  to the system path
import sys
sys.path.append('/home/adamsl/ottomator-agents/mem0-agent/iterations/python_tools/chroma_db_manager')


def create_collection(collection_name="agent_v2_collection"):
    # Initialize the Client
    client = Client()  

    # Create the collection
    try:
        collection = client.create_collection(collection_name)
        return f"Collection '{collection_name}' created successfully!"
    except Exception as e:
        return str(e)

def count_entries(collection_name="agent_v2_collection"):
    # Initialize the Client
    client = Client()  

    # Access the collection
    collection = client.get_collection(collection_name)

    # Count the number of entries
    entry_count = collection.count()
    return entry_count

def list_collections():
    # Initialize the Client
    client = Client()  

    # List collections
    collections = client.list_collections()
    return collections
