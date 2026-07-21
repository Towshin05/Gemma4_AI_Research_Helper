from sentence_transformers import SentenceTransformer


class EmbeddingGenerator:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
    def generate_embeddings(self, chunks):
        embeddings = self.model.encode(chunks, 
         convert_to_numpy=True,
         show_progress_bar=True)    
        
        return embeddings    
    

     