
class ChromaDbManager:
    def __init__(self):
        from chromadb import Client
        self.client = Client()

    def create_collection(self, collection_name='agent_v2_collection'):
        try:
            collection = self.client.create_collection(collection_name)
            return f"Collection '{collection_name}' created successfully!"
        except Exception as e:
            return str(e)

    def count_entries(self, collection_name='agent_v2_collection'):
        collection = self.client.get_collection(collection_name)
        entry_count = collection.count()
        return entry_count

    def list_collections(self):
        collections = self.client.list_collections()
        return collections
