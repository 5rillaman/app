import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Click Game</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }
            button {
                padding: 20px;
                font-size: 18px;
                margin: 20px;
                cursor: pointer;
            }
            #score {
                font-size: 24px;
                margin: 20px;
            }
        </style>
    </head>
    <body>
        <h1>Click the Button!</h1>
        <div id="score">Score: 0</div>
        <button id="click-button">Click Me!</button>
        <script>
            let score = 0;
            document.getElementById('click-button').addEventListener('click', () => {
                score += 1;
                document.getElementById('score').innerText = `Score: ${score}`;
            });
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
