# 🧠 Respuestas de las preguntas

## 📌 Paso 1: Modelado de Datos

### ● ¿Qué campos mínimos debería tener un evento de log de usuario?

Los campos mínimos que definí fueron:
- `"event_type"`: tipo de acción del usuario
- `"user_id"`: identificador del usuario
- `"timestamp"`: momento exacto de la acción

Opcionalmente incluí campos como:
- `"device"`: sistema o tipo de dispositivo
- `"app_version"`: versión de la aplicación móvil

---

### ● ¿Cómo se estructuraría un evento de "ver producto" vs uno de "añadir al carrito"?

Ambos comparten los campos comunes, pero:

- **`view_product`**:
```json
{
  "event_type": "view_product",
  "user_id": "user123",
  "timestamp": "2025-06-25T14:32:00Z",
  "product_id": "P001",
  "product_name": "Auriculares"
}
```

- **`add_to_cart`**:
```json
{
  "event_type": "add_to_cart",
  "user_id": "user123",
  "timestamp": "2025-06-25T14:35:00Z",
  "product_id": "P001",
  "quantity": 2,
  "price": 59.99
}
```
---
### ● ¿Qué campos serían obligatorios para todos los eventos?

- `event_type`

- `user_id`

- `timestamp`

Estos campos fueron validados en todos los tipos de eventos con `NotNullValidator`.
---

### ● ¿Qué campos podrían ser opcionales o específicos?

- `product_id`, `product_name`, `quantity`, `price` **→** específicos según el tipo de evento.

- `device`, `app_version` **→** opcionales, pero útiles para análisis adicionales.
---

### ✅ Resultado

Diseñé una clase base `LogEvent` con los campos comunes, y subclases como `ProductViewEvent` y `AddToCartEvent` con los campos específicos. Este diseño me permitió aplicar el Principio OCP (Abierto/Cerrado) para extender el sistema sin modificar las clases existentes.
---
---

## 1. ¿Cómo el Principio de Responsabilidad Única (SRP) hizo más fácil crear y mantener los validadores?

Cada validador implementa una única validación (campos nulos, tipo de evento, detalles del producto). Esto me permitió extender la cadena fácilmente, mantener el código aislado y probar cada regla por separado. Si un validador necesita cambiar, no afecta a los demás.

---

## 2. ¿Cómo se aplica el Principio Abierto/Cerrado (OCP) en su diseño?

Las subclases de `LogEvent` y los validadores están diseñados para extenderse sin modificar el código existente. Por ejemplo, puedo agregar nuevos tipos de eventos o nuevas reglas de validación sin tocar el código anterior, solo añadiendo nuevas clases y conectándolas.

---

## 3. ¿Qué ventajas ofrece el Patrón Factory Method en este escenario?

Centraliza la lógica de creación de objetos de eventos. Gracias al factory, el sistema no necesita saber qué tipo exacto de evento está llegando, solo cómo construirlo a partir de sus datos. Esto mejora la escalabilidad y desacopla el flujo de negocio de los detalles de implementación.

---

## 4. ¿Cómo el Patrón Chain of Responsibility simplifica la lógica de validación?

Permite encadenar validadores independientes, en lugar de usar condicionales anidados o funciones monolíticas. Si un validador falla, se detiene la cadena y se informa el error. Esto facilita agregar, remover o reordenar validadores sin romper el flujo.

---

## 5. ¿Cómo modelaría los eventos en una base de datos relacional vs una NoSQL?

- **Relacional**: usaría una tabla `eventos` con columnas comunes (`event_type`, `user_id`, `timestamp`) y campos opcionales o tablas auxiliares según el tipo de evento.
- **NoSQL**: almacenaría cada evento como un documento JSON completo. Esto me da más flexibilidad para manejar estructuras distintas por tipo sin romper esquema.
