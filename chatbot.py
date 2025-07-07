from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# OpenAIに質問内容を送信し、応答を獲得するメソッド
def get_chatgpt_response(prompt): 
    try:
        response = client.chat.completions.create( # ChatGPT APIを介し、ChatGPT からの回答を格納する変数
            model="gpt-3.5-turbo",          
            messages=[{"role": "user",     # ユーザの発話であると示す
            "content": prompt
            }]            # 質問内容を入れる変数
        )  

        # レスポンスを返す
        return response.choices[0].message.content # ChatGPT が生成した回答の中の一番最初のメッセージを取得する
        # messageとはChatGPT が生成したテキストやメッセージ
        # contentとはメッセージの内容
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"

# ここからチャットボットへの質問
question = input("ここに質問内容を入力してください: ")
print("あなたの質問:", question) 
answer = get_chatgpt_response(question) # ChatGPTを起動
print(answer) # ChatGPTからの答えを出力


