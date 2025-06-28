"""
Define los campos obligatorios comunes a todos los eventos del sistema.
"""


class Campos:
    """
    Contiene los campos que deben estar presentes y opcionales en todos los eventos, sin importar su tipo.

    Atributos:
        event_type: Tipo de evento registrado.
        user_id: Identificador del usuario que generó el evento.
        timestamp: Fecha y hora en que ocurrió el evento.
        device: Tipo de dispositivo.
        app_version: Versión de la aplicación.
        lista_campos_requeridos: Lista que agrupa todos los campos obligatorios comunes.
        lista_campos_opcionales: Lista que agrupa todos los campos opcionales.
    """

    event_type = 'event_type'
    user_id = 'user_id'
    timestamp = 'timestamp'
    device = 'device'
    app_version = 'app_version'

    lista_campos_requeridos = [event_type, user_id, timestamp]

    lista_campos_opcionales = [device, app_version]
