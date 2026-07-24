import chromadb


class ChromaManager:
    
    def __init__(self):
        self.client=chromadb.PersistentClient(path="chroma_db")
        self.collection=self.client.get_or_create_collection(name="resarch_papers")
        
    def add_documents(self, chunks, embeddings, paper_name):
        
        id=[]
        metadata=[]  
        
        for i in range(len(chunks)):
            id.append(f"{paper_name}_chunk_{i}")
            metadata.append({
                "paper_name": paper_name,
                "chunk_no": i
            })
            
        self.collection.add(
            documents=chunks, 
            embeddings=embeddings.tolist(), 
            metadatas=metadata, 
            ids=id)    
    def collection_count(self):
        return self.collection.count()    
    
    def search(self, query_embedding,k_top=15):
        results=self.collection.query(
            query_embeddings=query_embedding.tolist(),
            n_results=k_top,
        )
        return results
    
    def clear_database(self):
        self.client.delete_collection("research_papers")
        self.collection=self.client.create_collection("research_papers")
        