class ResponseFormatter:

    def format_response(self, answer, metadatas):

        paper_names = []

        for metadata in metadatas:

            paper = metadata["paper_name"]

            if paper not in paper_names:
                paper_names.append(paper)

        return {
            "answer": answer,
            "papers": paper_names,
            "num_sources": len(paper_names)
        }     