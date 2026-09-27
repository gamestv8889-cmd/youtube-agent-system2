import os
from google import genai

print("START")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API KEY NOT FOUND")
    raise SystemExit(1)

print("API KEY FOUND")

client = genai.Client(api_key=api_key)

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Say hello."
    )
    print("GEMINI WORKS")
    print(response.text)
except Exception as e:
    print("GEMINI ERROR:")
    print(type(e).__name__)
    print(str(e))
    raise