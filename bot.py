import config
import json
import requests
import openai
openai.api_key = OPENAI_API_KEY
def handle_message(message):
    # 提取消息文本
    text = message['text']

    # 使用 OpenAI API 生成回复
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    reply = response.choices[0].text.strip()
    return reply
def send_reply(token, open_id, text):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {token}"
    }
    url = "https://open.feishu.cn/open-apis/im/v1/messages"
    payload = {
        "open_id": open_id,
        "msg_type": "text",
        "content": {"text": text}
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()