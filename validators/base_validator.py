"""
Define la clase base para validadores y una excepción personalizada para errores de validación.
"""


class ValidationError(Exception):
    """
    Excepción personalizada para representar errores durante la validación de eventos.

    Args:
        message: Mensaje descriptivo del error de validación.
    """

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class BaseValidator:
    """
    Clase base para la construcción de validadores encadenados.

    Args:
        next_validator: Siguiente validador en la cadena. Si es None, la validación termina aquí.
        
    """

    def __init__(self, next_validator=None):
        self.next_validator = next_validator

    def validate(self, event):
        """
        Ejecuta la validación del evento y continúa con el siguiente validador, si existe.
        """
        self._validate(event)
        if self.next_validator:
            self.next_validator.validate(event)

    def _validate(self, event):
        """
        Método abstracto que debe ser implementado por cada clase concreta que extienda BaseValidator.
        """
        raise NotImplementedError('Debe implementar _validate() en el validador concreto')
