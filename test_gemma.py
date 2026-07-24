import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

client=genai.Client(api_key=api_key)

response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello world in 5 different languages."
)

print (response.text)

# import os

# from dotenv import load_dotenv
# from google import genai

# load_dotenv()

# client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# for model in client.models.list():
#     print(model.name)