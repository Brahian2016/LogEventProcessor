"""
Define la clase base para representar eventos genéricos del sistema.
"""

from datetime import datetime
from typing import Optional
from metadata.fields import Campos


class LogEvent:
    """
    Clase base para eventos registrados por el sistema. Contiene los atributos comunes
    a todos los tipos de eventos.

    Args:
        event_type: Tipo de evento.
        user_id: ID del usuario que genera el evento.
        timestamp: Fecha y hora del evento (formato ISO 8601).
        device: Dispositivo desde el cual se origina el evento.
        app_version: Versión de la aplicación utilizada.
        
    """

    def __init__(
        self,
        event_type: str,
        user_id: str,
        timestamp: str,
        device: Optional[str] = None,
        app_version: Optional[str] = None,
    ):
        self.event_type = event_type
        self.user_id = user_id
        self.timestamp = timestamp
        self.device = device
        self.app_version = app_version

    def is_valid(self) -> bool:
        """
        Retorna True por defecto. Esta función puede ser sobrescrita o utilizada por
        validadores externos para aplicar lógica personalizada.

        """
        return True

    def to_dict(self) -> dict:
        """
        Convierte el evento en un diccionario serializable utilizando
        los campos obligatorios definidos en la metadata.

        """
        campos = Campos.lista_campos_requeridos + Campos.lista_campos_opcionales

        return {campo: getattr(self, campo, None) for campo in campos}
