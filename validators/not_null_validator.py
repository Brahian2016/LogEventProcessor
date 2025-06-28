"""
Valida que los campos obligatorios del evento no estén vacíos ni ausentes.
"""

from validators.base_validator import BaseValidator, ValidationError
from metadata.fields import Campos


class NotNullValidator(BaseValidator):
    """
    Validador que asegura que los campos requeridos no sean nulos ni cadenas vacías.

    Args:
        required_fields: Lista de campos que deben estar presentes y no vacíos.
        next_validator: Siguiente validador en la cadena.
    """

    def __init__(self, required_fields=None, next_validator=None):
        super().__init__(next_validator)
        self.required_fields = required_fields or Campos.lista_campos_requeridos

    def _validate(self, event):
        """
        Verifica que todos los campos requeridos existan y no estén vacíos.
        Lanza una excepción si alguno falla la validación.
        """
        for field in self.required_fields:
            value = getattr(event, field, None)
            if value is None or (isinstance(value, str) and not value.strip()):
                raise ValidationError(
                    f"El campo obligatorio '{field}' está vacío o no existe."
                )
