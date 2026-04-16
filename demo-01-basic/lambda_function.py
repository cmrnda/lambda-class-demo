import json
import os
from datetime import datetime, timezone


APP_NAME = os.getenv("APP_NAME", "lambda-class-demo")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


def build_response(status_code: int, body: dict) -> dict:
    """
    Construye una respuesta estándar en formato JSON.
    """
    return {
        "statusCode": status_code,
        "body": json.dumps(body, ensure_ascii=False)
    }


def lambda_handler(event, context):
    """
    Demo 1:
    Lambda básica que recibe un evento manual y devuelve un saludo.
    """
    nombre = event.get("nombre", "mundo")
    ahora = datetime.now(timezone.utc).isoformat()

    print(json.dumps({
        "level": LOG_LEVEL,
        "app": APP_NAME,
        "message": "Invocación recibida en demo-01-basic",
        "timestamp_utc": ahora,
        "aws_request_id": getattr(context, "aws_request_id", None)
    }, ensure_ascii=False))

    return build_response(200, {
        "ok": True,
        "demo": "basic",
        "mensaje": f"Hola, {nombre}. Bienvenido a AWS Lambda.",
        "timestamp_utc": ahora
    })
