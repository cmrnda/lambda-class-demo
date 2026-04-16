import json
import os
from datetime import datetime, timezone

APP_NAME = os.getenv("APP_NAME", "lambda-class-demo")
DEFAULT_NAME = os.getenv("DEFAULT_NAME", "mundo")

def build_response(status_code: int, body: dict) -> dict:
    """
    Respuesta HTTP estándar para Function URL.
    """
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json; charset=utf-8"
        },
        "body": json.dumps(body, ensure_ascii=False)
    }

def get_query_param(event: dict, key: str, default=None):
    """
    Obtiene un query param de forma segura.
    """
    query_params = event.get("queryStringParameters") or {}
    return query_params.get(key, default)

def lambda_handler(event, context):
    """
    Demo 2:
    Lambda expuesta por HTTP usando Function URL.
    """
    ahora = datetime.now(timezone.utc).isoformat()
    nombre = get_query_param(event, "nombre", DEFAULT_NAME)

    print(json.dumps({
        "app": APP_NAME,
        "message": "Invocación HTTP recibida en demo-02-function-url",
        "timestamp_utc": ahora,
        "method": ((event.get("requestContext") or {}).get("http") or {}).get("method"),
        "path": ((event.get("requestContext") or {}).get("http") or {}).get("path"),
        "aws_request_id": getattr(context, "aws_request_id", None)
    }, ensure_ascii=False))

    return build_response(200, {
        "ok": True,
        "demo": "function-url",
        "mensaje": f"Hola, {nombre}. Esta respuesta viene por HTTP con Function URL.",
        "timestamp_utc": ahora
    })
