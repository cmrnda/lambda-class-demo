# AWS Lambda Class Demo

Repositorio de apoyo para una clase introductoria de **AWS Lambda** y **Serverless**.

## Objetivo

Mostrar tres formas sencillas de trabajar con AWS Lambda:

1. **Demo 1:** Ejecutar una función con un evento manual.
2. **Demo 2:** Exponer una función por HTTP usando Function URL.
3. **Demo 3:** Ejecutar una función automáticamente con EventBridge Scheduler.

## Requisitos

- Cuenta de AWS con acceso a AWS Lambda.
- Python 3.x instalado (para pruebas locales).
- Editor de código (recomendado: Visual Studio Code).
- Ganas de aprender.

## Estructura del proyecto

```
lambda-class-demo/
├── README.md                ← este archivo
├── .gitignore               ← exclusiones comunes
├── requirements.txt         ← dependencias (vacío en estas demos)
├── docs/
│   └── clase-guia.md        ← apuntes para la exposición
├── events/
│   ├── basic-event.json     ← evento de ejemplo para la demo básica
│   ├── function-url-event.json ← evento de ejemplo para Function URL
│   └── scheduler-event.json ← evento de ejemplo para Scheduler
├── demo-01-basic/
│   └── lambda_function.py   ← código de la demo básica
├── demo-02-function-url/
│   └── lambda_function.py   ← código de la demo HTTP
└── demo-03-scheduler/
    └── lambda_function.py   ← código de la demo automática
```

## Buenas prácticas aplicadas

Estas demos aplican buenas prácticas recomendadas por AWS:

- **Funciones pequeñas y con una sola responsabilidad.** Cada archivo `lambda_function.py` contiene una función que realiza una tarea específica.
- **Variables de entorno para configuración.** Se usan variables como `APP_NAME` o `TASK_NAME` en lugar de codificar valores en el código.
- **Respuestas consistentes en JSON.** Todas las funciones devuelven un diccionario con `statusCode` y `body` para mantener coherencia en las integraciones HTTP.
- **Logging estructurado.** Se utiliza `print` para registrar eventos en formato JSON, lo que facilita su análisis en CloudWatch Logs.
- **Sin secretos hardcodeados.** No se incluyen claves ni contraseñas; cualquier dato sensible debe gestionarse con AWS Secrets Manager.

## Despliegue sugerido

Crea una función Lambda por cada carpeta de demo. Sube el archivo `lambda_function.py` y utiliza `lambda_function.lambda_handler` como handler. No necesitas incluir dependencias externas para estas pruebas.

## Orden recomendado para la clase

1. **Demo 1 – básica:** muestra el modelo de evento y respuesta de Lambda.
2. **Demo 2 – Function URL:** expone la función como un endpoint HTTP.
3. **Demo 3 – Scheduler:** automatiza la ejecución en un horario.

## Nota sobre costos

Estas demos están pensadas para mantenerse en la capa gratuita o con costos casi nulos, utilizando únicamente:

- AWS Lambda: 1 millón de peticiones gratuitas al mes y 400 000 GB‑segundos de cómputo gratis.
- Function URL: no tiene costo adicional más allá de la ejecución de Lambda.
- EventBridge Scheduler: 14 millones de invocaciones gratuitas al mes.

Asegúrate de eliminar los Schedules cuando ya no los necesites y evita crear recursos como NAT Gateway o VPC innecesarias para no incurrir en cargos.