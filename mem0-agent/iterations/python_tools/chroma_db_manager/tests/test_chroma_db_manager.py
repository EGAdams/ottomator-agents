# add ~/ottomator-agents/mem0-agent/iterations/python_tools/chroma_db_manager$  to the system path
import sys
sys.path.append('/home/adamsl/ottomator-agents/mem0-agent/iterations/python_tools/')

import unittest
from chroma_db_manager.ChromaDbManager import ChromaDbManager

class TestChromaDbManager(unittest.TestCase):
    def setUp(self):
        self.manager = ChromaDbManager()
        # Create a test collection before each test
        self.manager.create_collection("test_collection")

    def test_create_collection(self):
        response = self.manager.create_collection("test_collection")
        # Check if the collection was created or already exists
        self.assertTrue("created successfully" in response or "already exists" in response)

    def test_count_entries(self):
        count = self.manager.count_entries("test_collection")
        self.assertIsInstance(count, int)

    def test_list_collections(self):
        collections = self.manager.list_collections()
        self.assertIsInstance(collections, list)

if __name__ == '__main__':
    unittest.main()
