import os

print("TEST START")

key = os.getenv("GEMINI_API_KEY")

if key:
    print("GEMINI_API_KEY FOUND")
else:
    print("GEMINI_API_KEY NOT FOUND")

print("TEST END")