import os
import google.generativeai as genai
import sys

# تنظیم API Key
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# دریافت سوال از آرگومان‌های ورودی
if len(sys.argv) < 2:
    print("No question provided.")
    sys.exit(1)

user_question = sys.argv[1]

# مدل را انتخاب کنید (gemini-1.5-flash برای سرعت یا gemini-1.5-pro برای دقت بیشتر)
model = genai.GenerativeModel('gemini-1.5-flash')

try:
    # ارسال درخواست به جمینای
    response = model.generate_content(user_question)
    answer = response.text

    # ذخیره در فایل
    filename = "gemini_response.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Question\n{user_question}\n\n")
        f.write(f"# Answer\n{answer}\n")
    
    print(f"Response saved to {filename}")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
