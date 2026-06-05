from google import genai
import os

client = os.getenv("GOOGLE_API_KEY")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="You are a helpful assistant that teach OOP in Python and Java. Please, response in Brazilian Portuguese. What is OOP? Give me an example in Python and Java.",
)

print(response.text)