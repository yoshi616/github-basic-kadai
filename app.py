from flask import Flask, request, render_template

# .envファイルからキーを取得するコード
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv() # .envファイルを読み込む
api_key = os.getenv("OPENAI_API_KEY") 
client = OpenAI(api_key=api_key)
app = Flask(__name__)

def get_chatgpt_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    answer =""
    if request.method == "POST":
        user_input = request.form["message"]
        answer = get_chatgpt_response(user_input)
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
