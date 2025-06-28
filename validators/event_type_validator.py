"""
Valida que el tipo de evento recibido sea uno de los tipos permitidos por el sistema.
"""

from validators.base_validator import BaseValidator, ValidationError
from metadata.event_types import TipoEventosValidos
from metadata.messages import MensajesGenerales


class EventTypeValidator(BaseValidator):
    """
    Validador que verifica si el tipo de evento está dentro de los tipos válidos definidos.

    Args:
        next_validator: Siguiente validador en la cadena. Si es None, se detiene aquí.
    """

    def __init__(self, next_validator=None):
        super().__init__(next_validator)
        self.valid_event_types = TipoEventosValidos.lista_tipo_eventos

    def _validate(self, event):
        """
        Lanza un error si el tipo de evento no se encuentra en la lista de tipos válidos.
        """
        if event.event_type not in self.valid_event_types:
            raise ValidationError(
                MensajesGenerales.tipo_evento_invalido.format(
                    tipo=event.event_type, validos=', '.join(self.valid_event_types)
                )
            )
