from flask import Flask
import os

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Hello Docker World")


@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{APP_NAME}</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}

            body {{
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: 'Segoe UI', Roboto, sans-serif;
                background: linear-gradient(135deg, #0f172a, #1e293b);
                color: #f1f5f9;
            }}

            .card {{
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
                padding: 48px 64px;
                text-align: center;
                backdrop-filter: blur(6px);
                box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
            }}

            .badge {{
                display: inline-block;
                padding: 4px 12px;
                border-radius: 999px;
                background: #2563eb33;
                color: #60a5fa;
                font-size: 12px;
                letter-spacing: 1px;
                text-transform: uppercase;
                margin-bottom: 16px;
            }}

            h1 {{
                font-size: 2.2rem;
                font-weight: 600;
                margin-bottom: 8px;
            }}

            p {{
                color: #94a3b8;
                font-size: 0.95rem;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <span class="badge">Running in Docker</span>
            <h1>{APP_NAME}</h1>
            <p>Served by Flask · Deployed via ECR pipeline</p>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)