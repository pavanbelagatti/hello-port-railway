from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello from Port + Railway</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, sans-serif;
                max-width: 600px;
                margin: 80px auto;
                padding: 20px;
                text-align: center;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                min-height: 80vh;
            }
            h1 { font-size: 3em; margin-bottom: 0.2em; }
            p { font-size: 1.2em; opacity: 0.9; }
            .badge {
                display: inline-block;
                background: rgba(255,255,255,0.2);
                padding: 6px 16px;
                border-radius: 20px;
                margin-top: 20px;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <h1>Hello from Port!</h1>
        <p>Deployed to Railway via the DevOps Platform Agent.</p>
        <div class="badge">powered by Flask - scaffolded by AI</div>
    </body>
    </html>
    '''

@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
