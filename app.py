import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Render!"

if __name__ == '__main__':
    # Renderが提供するPORT環境変数を取得
    port = int(os.environ.get('PORT', 5000))  # デフォルト値は5000
    app.run(host='0.0.0.0', port=port)