from qdrant_client import QdrantClient

# Initialize the client
client = QdrantClient(url="http://localhost:6333")

# Check connection by fetching collections
try:
    collections = client.get_collections()
    print("✅ Successfully connected to Qdrant!")
    print(f"Current collections: {collections}")
except Exception as e:
    print(f"❌ Connection failed: {e}")
