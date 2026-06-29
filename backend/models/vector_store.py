import faiss
import numpy as np

class VectorStore:

    def __init__(self):

        self.dimension = 384

        self.index = faiss.IndexFlatL2(
            self.dimension
        )

        self.texts = []

    def add(self, embedding, text):

        embedding = np.array(
            [embedding]
        ).astype("float32")

        self.index.add(embedding)

        self.texts.append(text)

    def search(self, embedding):

        embedding = np.array(
            [embedding]
        ).astype("float32")

        distance, index = self.index.search(
            embedding,
            1
        )

        return distance[0][0], index[0][0]