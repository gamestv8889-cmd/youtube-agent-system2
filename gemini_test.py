import os
from google import genai

print("TEST START")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: API KEY NOT FOUND")
    raise SystemExit(1)

print("API KEY FOUND")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello in one short sentence."
)

print("GEMINI SUCCESS")
print(response.text)