import json
import os
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

def load_catalog(filepath='data/shl_catalog.json'):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_text_representation(item):
    return f"{item['name']} {item['test_type']} {item['duration']} " \
           f"Remote Testing: {item['remote_testing']} Adaptive: {item['adaptive_support']}"

def embed_catalog(catalog):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    texts = [create_text_representation(item) for item in catalog]
    embeddings = model.encode(texts, convert_to_numpy=True)
    return embeddings

def save_index(embeddings, catalog, index_path='data/faiss_index.bin', meta_path='data/catalog_metadata.json'):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    faiss.write_index(index, index_path)
    
   
    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(catalog, f, indent=2)

def build_catalog_index():
    catalog = load_catalog()
    embeddings = embed_catalog(catalog)
    save_index(embeddings, catalog)
    print(f"[✓] Index built and saved successfully with {len(catalog)} entries.")

if __name__ == "__main__":
    build_catalog_index()
