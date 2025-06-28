"""
Define el evento correspondiente a la acción de agregar un producto al carrito.
"""

from models.base_event import LogEvent
from metadata.fields_by_event import CamposPorTipoEvento


class AddToCartEvent(LogEvent):
    """
    Representa un evento donde un usuario agrega un producto al carrito.

    Args:
        event_type: Tipo de evento.
        user_id: ID del usuario que realiza la acción.
        timestamp: Fecha y hora del evento.
        product_id: ID del producto agregado.
        quantity: Cantidad del producto.
        price: Precio unitario del producto.
        device: Dispositivo desde el cual se generó el evento.
        app_version: Versión de la aplicación usada.
        

    """

    def __init__(
        self,
        event_type: str,
        user_id: str,
        timestamp: str,
        product_id: str,
        quantity: int,
        price: float,
        device: str = None,
        app_version: str = None,
    ):
        super().__init__(event_type, user_id, timestamp, device, app_version)
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> dict:
        """
        Convierte el evento en un diccionario, incluyendo los campos específicos
        del evento 'add_to_cart' obtenidos dinámicamente desde la metadata.

        """
        base = super().to_dict()

        campos_evento = CamposPorTipoEvento.campos_especificos.get(self.event_type, [])
        valores_evento = {campo: getattr(self, campo, None) for campo in campos_evento}

        base.update(valores_evento)
        return base
