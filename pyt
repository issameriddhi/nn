!pip install google-generativeai
from google import genai

client = genai.Client(api_key="AIzaSyDffC2W4CxJDt6KI5UWStsQgO5SqfoYnRw")
#key = AIzaSyBLINktRwmczcCFd2ysg546Q2pJ1Of9T4c
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=input("Q: ")
    )
    print(response.text)

except Exception as e:
    print("Error:", e)




