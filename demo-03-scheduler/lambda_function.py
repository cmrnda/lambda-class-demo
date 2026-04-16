import json
import os
from datetime import datetime, timezone

APP_NAME = os.getenv("APP_NAME", "lambda-class-demo")
TASK_NAME = os.getenv("TASK_NAME", "tarea-programada")

def build_response(status_code: int, body: dict) -> dict:
    """
    Construye una respuesta consistente.
    """
    return {
        "statusCode": status_code,
        "body": json.dumps(body, ensure_ascii=False)
    }

def lambda_handler(event, context):
    """
    Demo 3:
    Lambda ejecutada automáticamente por EventBridge Scheduler.
    """
    ahora = datetime.now(timezone.utc).isoformat()
    source = event.get("source", "desconocido")
    detail_type = event.get("detail-type", "sin detalle")

    print(json.dumps({
        "app": APP_NAME,
        "message": "Invocación automática recibida en demo-03-scheduler",
        "task_name": TASK_NAME,
        "timestamp_utc": ahora,
        "source": source,
        "detail_type": detail_type,
        "aws_request_id": getattr(context, "aws_request_id", None)
    }, ensure_ascii=False))

    return build_response(200, {
        "ok": True,
        "demo": "scheduler",
        "mensaje": f"La tarea '{TASK_NAME}' se ejecutó correctamente.",
        "timestamp_utc": ahora,
        "source": source,
        "detail_type": detail_type
    })
