# 📝 Event Log Processor

Este proyecto simula un sistema de procesamiento de eventos de usuario (logs) como los que se generan en aplicaciones móviles. Aplica principios de diseño orientado a objetos (OOP), SOLID y patrones de diseño como Factory y Chain of Responsibility.

## 🚀 Estructura del proyecto

```text
event_processor/
├── main.py # Script principal de ejecución
│
├── metadata/                    # Configuración y constantes del sistema
│   ├── __init__.py
│   ├── event_types.py           # Tipos válidos de eventos
│   ├── fields.py                # Campos obligatorios generales
│   ├── fields_by_event.py       # Campos requeridos por tipo de evento
│   └── messages.py              # Mensajes generales centralizados
│
├── models/ # Modelos de eventos
│ ├── base_event.py
│ ├── product_view_event.py
│ └── add_to_cart_event.py
│
├── factory/
│ └── event_factory.py # Fábrica para crear instancias de eventos
│
├── validators/ # Validadores encadenados
│ ├── base_validator.py
│ ├── not_null_validator.py
│ ├── event_type_validator.py
│ └── product_details_validator.py
│
├── examples/
│ └── test_events.py # Lista de eventos de prueba
└── requirements.txt # Dependencias del proyecto
```

## 📚 Conceptos aplicados

- Programación Orientada a Objetos (OOP)
- Principios SOLID:
  - SRP: cada clase tiene una sola responsabilidad
  - OCP: nuevas clases sin modificar las existentes
- Patrones de diseño:
  - Factory Method
  - Chain of Responsibility

## ✅ Cómo ejecutar

1. Clona o descarga el repositorio.
2. Asegúrate de tener Python 3.8 o superior.
3. Instala dependencias (Este ejercicio no cuenta con dependencias):
```bash
pip install -r requirements.txt
```
4. Ejecuta el archivo principal:
```bash
python main.py
```