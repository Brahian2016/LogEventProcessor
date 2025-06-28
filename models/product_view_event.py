"""
Define el evento correspondiente a la visualización de un producto por parte del usuario.
"""

from models.base_event import LogEvent
from metadata.fields_by_event import CamposPorTipoEvento


class ProductViewEvent(LogEvent):
    """
    Representa un evento donde un usuario visualiza un producto.

    Args:
        event_type: Tipo de evento.
        user_id: ID del usuario que realiza la acción.
        timestamp: Fecha y hora del evento.
        product_id: ID del producto visualizado.
        product_name: Nombre del producto visualizado.
        device: Dispositivo desde el cual se generó el evento.
        app_version: Versión de la aplicación usada.
        
    """

    def __init__(
        self,
        event_type: str,
        user_id: str,
        timestamp: str,
        product_id: str,
        product_name: str,
        device: str = None,
        app_version: str = None,
    ):
        super().__init__(event_type, user_id, timestamp, device, app_version)
        self.product_id = product_id
        self.product_name = product_name

    def to_dict(self) -> dict:
        """
        Convierte el evento en un diccionario, incluyendo los campos específicos
        del evento 'product_view_event' obtenidos dinámicamente desde la metadata.

        """
        base = super().to_dict()

        campos_evento = CamposPorTipoEvento.campos_especificos.get(self.event_type, [])
        valores_evento = {campo: getattr(self, campo, None) for campo in campos_evento}

        base.update(valores_evento)
        return base
