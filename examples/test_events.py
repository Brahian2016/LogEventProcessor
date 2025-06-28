test_events = [
    # Válido: vista de producto
    {
        "event_type": "view_product",
        "user_id": "user123",
        "timestamp": "2025-06-25T14:32:00Z",
        "product_id": "P001",
        "product_name": "Auriculares Sony",
        "device": "Android",
        "app_version": "1.0.0",
    },
    # Válido: añadir al carrito
    {
        "event_type": "add_to_cart",
        "user_id": "user456",
        "timestamp": "2025-06-25T15:10:00Z",
        "product_id": "P002",
        "quantity": 2,
        "price": 99.99,
    },
    # Inválido: falta user_id
    {
        "event_type": "view_product",
        "timestamp": "2025-06-25T14:32:00Z",
        "product_id": "P003",
        "product_name": "Mouse Logitech",
    },
    # Inválido: tipo no reconocido
    {"event_type": "purchase", "user_id": "user789", "timestamp": "2025-06-25T15:00:00Z"},
    # Inválido: falta product_id en evento de producto
    {
        "event_type": "add_to_cart",
        "user_id": "user999",
        "timestamp": "2025-06-25T16:00:00Z",
        "quantity": 1,
        "price": 49.99,
    },
]
