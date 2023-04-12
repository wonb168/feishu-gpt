from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    event = data['event']

    # 处理事件类型
    if event['type'] == 'message':
        # 调用处理消息的函数
        reply = handle_message(event)

        # 获取 App Access Token
        app_access_token = get_app_access_token(APP_ID, APP_SECRET)

        # 向发送者发送回复
        send_reply(app_access_token, event['open_id'], reply)

    return jsonify({'challenge': data['challenge']})