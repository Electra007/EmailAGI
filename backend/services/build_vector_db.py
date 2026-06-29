import pandas as pd
import pickle

from backend.models.embeddings import EmbeddingModel
from backend.models.vector_store import VectorStore

embedder = EmbeddingModel()

store = VectorStore()

df = pd.read_csv(
    "synthetic_data/banking_emails.csv"
)

for _, row in df.iterrows():

    text = row["subject"] + " " + row["body"]

    embedding = embedder.encode(text)

    store.add(
        embedding,
        text
    )

with open(
    "backend/models/vector_db.pkl",
    "wb"
) as f:

    pickle.dump(
        store,
        f
    )

print("Vector Database Created!")