import os
from datetime import datetime, timezone

APP_NAME = os.getenv("APP_NAME", "lambda-class-demo")
DEFAULT_NAME = os.getenv("DEFAULT_NAME", "mundo")

def get_query_param(event: dict, key: str, default=None):
    query_params = event.get("queryStringParameters") or {}
    return query_params.get(key, default)

def lambda_handler(event, context):
    ahora = datetime.now(timezone.utc).isoformat()
    nombre = get_query_param(event, "nombre", DEFAULT_NAME)

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Demo Lambda</title>
        <style>
            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
            }}

            body {{
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #0f172a, #1e293b, #2563eb);
                color: white;
                padding: 24px;
            }}

            .card {{
                width: 100%;
                max-width: 700px;
                background: rgba(255, 255, 255, 0.10);
                border: 1px solid rgba(255, 255, 255, 0.18);
                backdrop-filter: blur(10px);
                border-radius: 20px;
                padding: 40px;
                box-shadow: 0 20px 50px rgba(0, 0, 0, 0.25);
                text-align: center;
            }}

            .badge {{
                display: inline-block;
                margin-bottom: 18px;
                padding: 8px 14px;
                border-radius: 999px;
                background: rgba(255,255,255,0.16);
                font-size: 14px;
            }}

            h1 {{
                font-size: 42px;
                margin-bottom: 16px;
            }}

            p {{
                font-size: 18px;
                line-height: 1.6;
                color: #e2e8f0;
                margin-bottom: 14px;
            }}

            .highlight {{
                color: #facc15;
                font-weight: bold;
            }}

            .footer {{
                margin-top: 22px;
                font-size: 14px;
                color: #cbd5e1;
            }}

            code {{
                background: rgba(255,255,255,0.12);
                padding: 4px 8px;
                border-radius: 8px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <div class="badge">AWS Lambda + Function URL</div>
            <h1>Hola desde Lambda 🚀</h1>
            <p>Bienvenido, <span class="highlight">{nombre}</span>.</p>
            <p>Esta página HTML fue generada directamente desde una función Lambda.</p>
            <p>Aplicación: <code>{APP_NAME}</code></p>
            <div class="footer">
                Generado en UTC: {ahora}
            </div>
        </div>
    </body>
    </html>
    """

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html; charset=utf-8"
        },
        "body": html
    }
