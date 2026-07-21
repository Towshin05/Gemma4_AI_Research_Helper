class PromptBuilder:
    def build_prompt(self,intent, question,documents, metadatas):
        context=""
        
        for document, metadata in zip(documents, metadatas):
            context+=f"""
Paper: {metadata['paper_name']}
Chunk {metadata['chunk_no']}
            
            
{document}
            
            """
            prompt = f"""
            
You are a research assistant. You have been provided with the following context from a research paper:
If the answer to the question is not present in the context, please respond with "I could not find sufficient information in the provided context to answer your question." Do not make up an answer.


Context:
    {context}
    
    Question: {question}
    
    Answer:
        """
        return prompt
    def summary_prompt(self, context):
        pass
    def comparison_prompt(self, context):
        pass
    def limitations_prompt(self, question, documents, metadatas):
        pass
    def future_work_prompt(self, question, documents, metadatas):
        pass
    def research_gap_prompt(self, question, documents, metadatas):
        pass
    def methodology_prompt(self, question, documents, metadatas):
        pass
    def suggested_research_prompt(self, question, documents, metadatas):
        pass
    
    def general_prompt(self, question, documents, metadatas):
        pass
    
    