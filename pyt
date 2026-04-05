!pip install google-generativeai
from google import genai

client = genai.Client(api_key="insert_api_key")

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",   
        contents=input("Q: ")
    )
    print(response.text)

except Exception as e:
    print("Error:", e)


