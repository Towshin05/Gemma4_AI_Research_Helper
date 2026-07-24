# import os
# from dotenv import load_dotenv

# from google import genai


# class GemmaClient:
#     def __init__(self):
#         load_dotenv()
        
#         self.api_key=os.getenv("GOOGLE_API_KEY")
#         self.client=genai.Client(api_key=self.api_key)
#         self.model="gemini-2.5-flash"
#     def generate_response(self, prompt):
#         response=self.client.models.generate_content(
#             model=self.model,
#             contents=prompt
#         )
        
#         return response.text


import os
from dotenv import load_dotenv
from openai import OpenAI


class GemmaClient:
    def __init__(self):
        load_dotenv()

        self.client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
        )

        self.model = "google/gemma-4-26b-a4b-it:free"

    def generate_response(self, prompt):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=4096,
        )

        return response.choices[0].message.content
    
    