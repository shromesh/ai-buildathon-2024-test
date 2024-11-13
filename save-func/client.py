import requests
import json

# エンドポイントURL
url = "https://us-central1-ai-buildathon-test-nov9-1.cloudfunctions.net/store_prompt_and_response"

# サンプルデータ
data = {
    "user_name": "SampleUser123",
    "data": [
        {
            "system_prompt": "You are an AI that provides helpful responses.",
            "user_prompt": "What is the capital of France?",
            "completion": "The capital of France is Paris.",
        },
        {
            "system_prompt": "You are a supportive assistant for language learning.",
            "user_prompt": "Translate 'Good morning' to Japanese.",
            "completion": "おはようございます。",
        },
        {
            "system_prompt": "You are a tutor that helps with basic math problems.",
            "user_prompt": "What is 15 + 27?",
            "completion": "15 + 27 is 42.",
        },
    ],
}

# POSTリクエストの送信
response = requests.post(
    url, headers={"Content-Type": "application/json"}, data=json.dumps(data)
)

# レスポンスの表示
if response.status_code == 200:
    print("Success:", response.text)
else:
    print("Error:", response.status_code, response.text)

## Cloud Run 関数からFirestoreへのアクセスは特に設定せずにできた。デフォルトのロールでいけるのか。
