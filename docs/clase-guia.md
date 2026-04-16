# Guía rápida de clase

Esta guía resume los puntos clave que se cubrirán en la clase práctica sobre AWS Lambda y Serverless. Puedes usarla como referencia al exponer o como material complementario para los estudiantes.

## Demo 1 – función básica

Explica:

- **Qué es una función Lambda.** Un fragmento de código que se ejecuta en respuesta a un evento.
- **Qué es un evento.** Un objeto JSON que contiene los datos de entrada para la función.
- **Qué devuelve Lambda.** Un diccionario con `statusCode` y `body` para las integraciones HTTP.

### Evento de ejemplo

El archivo `events/basic-event.json` contiene un ejemplo de evento sencillo:

```json
{
  "nombre": "Genesis"
}
```

## Demo 2 – Function URL

Explica:

- **Qué es Function URL.** Un endpoint HTTP dedicado para una función Lambda, sin necesidad de API Gateway.
- **Cómo pasar parámetros por URL.** Usando `queryStringParameters` dentro del evento.
- **Cómo devolver una respuesta JSON.** Incluyendo headers como `Content-Type`.

### Evento HTTP de ejemplo

El archivo `events/function-url-event.json` muestra el formato del evento que Lambda recibe cuando se invoca mediante HTTP:

```json
{
  "version": "2.0",
  "routeKey": "$default",
  "rawPath": "/",
  "rawQueryString": "nombre=Genesis",
  "queryStringParameters": {
    "nombre": "Genesis"
  },
  "requestContext": {
    "http": {
      "method": "GET",
      "path": "/"
    }
  }
}
```

## Demo 3 – Scheduler

Explica:

- **Qué es EventBridge Scheduler.** Un servicio para programar ejecuciones de Lambda en horarios específicos.
- **Cómo automatizar tareas.** Configura un schedule recurrente para que la función se ejecute sola.
- **Casos de uso.** Reportes automáticos, limpieza de datos, recordatorios, etc.

### Evento de ejemplo para Scheduler

El archivo `events/scheduler-event.json` contiene un ejemplo de evento que llega a la función cuando es invocada por un Schedule:

```json
{
  "source": "aws.scheduler",
  "detail-type": "Scheduled Event"
}
```

## Buenas prácticas para mencionar

- Diseñar funciones pequeñas y con una sola responsabilidad.
- Registrar información útil en los logs usando `print` con formato JSON.
- Usar variables de entorno para configuraciones como nombres de aplicación o tareas.
- Evitar hardcodear secretos; en su lugar, usar AWS Secrets Manager.
- Revisar los logs en CloudWatch para depurar y verificar las ejecuciones.
- No dejar schedules activos una vez terminada la demostración.

## Malas prácticas para advertir

- Crear una función que realice demasiadas tareas diferentes.
- Hardcodear claves o tokens en el código.
- Olvidar asignar permisos mínimos necesarios en el execution role.
- Incluir la función en una VPC sin justificación, lo que podría generar costos adicionales.
- Olvidar revisar los límites de concurrencia o el número de ejecuciones en la capa gratuita.
