import chromadb


class ChromaManager:
    
    def __init__(self):
        self.client=chromadb.PersistentClient(path="vector_db")
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