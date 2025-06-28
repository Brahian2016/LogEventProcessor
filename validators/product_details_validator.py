"""
Valida que el campo 'product_id' esté presente en los eventos que lo requieren.
"""

from validators.base_validator import BaseValidator, ValidationError
from metadata.fields_by_event import CamposPorTipoEvento
from metadata.event_types import TipoEventosValidos


class ProductDetailsValidator(BaseValidator):
    """
    Validador que verifica la presencia de 'product_id' en eventos que lo requieren.

    Args:
        applicable_event_types: Conjunto de tipos de evento donde se debe validar 'product_id'.
        next_validator: Siguiente validador en la cadena.
    """

    def __init__(self, applicable_event_types=None, next_validator=None):
        super().__init__(next_validator)
        self.applicable_event_types = applicable_event_types or {
            TipoEventosValidos.view_product,
            TipoEventosValidos.add_to_cart,
        }

    def _validate(self, event):
        """
        Lanza un error si 'product_id' no está presente o está vacío en eventos aplicables.
        """
        if event.event_type in self.applicable_event_types:
            if not hasattr(event, CamposPorTipoEvento.product_id) or not event.product_id:
                raise ValidationError(
                    f"'{CamposPorTipoEvento.product_id}' es obligatorio para eventos tipo '{event.event_type}'"
                )
