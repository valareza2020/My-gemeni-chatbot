import os
import sys
from google import genai

# دریافت API Key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY is not set.")
    sys.exit(1)

# دریافت سوال
if len(sys.argv) < 2:
    print("No question provided.")
    sys.exit(1)

user_question = sys.argv[1]

# راه‌اندازی کلاینت جدید گوگل
client = genai.Client(api_key=api_key)

try:
    # ارسال درخواست به مدل جدید
    response = client.models.generate_content(
        model="gemini-1.5-flash", 
        contents=user_question
    )
    
    answer = response.text

    # ذخیره در فایل
    filename = "gemini_response.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Question\n{user_question}\n\n")
        f.write(f"# Answer\n{answer}\n")
    
    print(f"Response saved to {filename}")

except Exception as e:
    print(f"Error occurred: {e}")
    sys.exit(1)
