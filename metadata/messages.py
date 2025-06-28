"""
Define los mensajes generales utilizados durante el proceso de validación de eventos.
"""


class MensajesGenerales:
    """
    Contiene los mensajes de éxito, error y excepciones usados por el sistema de validación.

    Atributos:
        evento_valido: Mensaje para eventos válidos.
        campo_obligatorio: Mensaje cuando un campo obligatorio está vacío o ausente.
        tipo_evento_invalido: Mensaje para tipo de evento no permitido.
        product_id_faltante: Mensaje cuando falta 'product_id' en eventos específicos.
        error_evento_desconocido: Mensaje para eventos no reconocidos por el sistema.
        error_inesperado: Mensaje para errores no controlados.
        evento_invalido: Mensaje general para eventos inválidos.

    """

    # ✅ Mensajes de éxito
    evento_valido = '✅ Evento válido: {evento}'

    # ❌ Mensajes de error (validaciones)
    campo_obligatorio = 'El campo obligatorio "{campo}" está vacío o no existe.'
    tipo_evento_invalido = 'Tipo de evento inválido: "{tipo}". Tipos válidos: {validos}'
    product_id_faltante = '"product_id" es obligatorio para eventos tipo "{tipo_evento}"'

    # 🚨 Errores inesperados
    error_evento_desconocido = 'Tipo de evento no soportado: "{event_type}"'
    error_inesperado = '🚨 Error inesperado: {error}'
    evento_invalido = '❌ Evento inválido: {mensaje}'
