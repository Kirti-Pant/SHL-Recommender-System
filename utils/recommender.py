import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_PATH = "data/faiss_index.bin"
META_PATH = "data/catalog_metadata.json"

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index(INDEX_PATH)

with open(META_PATH, 'r', encoding='utf-8') as f:
    metadata = json.load(f)

def recommend_assessments(query, top_k=5):

    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)
    
    results = []
    for idx in indices[0]:
        if idx < len(metadata):
            results.append(metadata[idx])
    return results

if __name__ == "__main__":
    query = "Looking for a personality and cognitive test under 30 minutes"
    recommendations = recommend_assessments(query)
    for i, item in enumerate(recommendations, 1):
        print(f"\n🔹 Recommendation {i}")
        print(f"Name: {item['name']}")
        print(f"URL: {item['url']}")
        print(f"Remote Testing: {item['remote_testing']}")
        print(f"Adaptive: {item['adaptive_support']}")
        print(f"Duration: {item['duration']}")
        print(f"Type: {item['test_type']}")
