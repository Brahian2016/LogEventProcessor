"""
Este módulo construye una cadena de validadores para eventos siguiendo el
patrón de cadena de responsabilidad (Chain of Responsibility) y ejecuta un
proceso de validación sobre una lista de eventos de prueba predefinidos.

"""

from factory.event_factory import EventFactory
from validators.not_null_validator import NotNullValidator
from validators.event_type_validator import EventTypeValidator
from validators.product_details_validator import ProductDetailsValidator
from validators.base_validator import ValidationError
from examples.test_events import test_events
from metadata.messages import MensajesGenerales


def build_validator_chain() -> NotNullValidator:
    """
    Construye la cadena de validadores utilizando el patrón de cadena de responsabilidad.

    Returns:
        El validador inicial de la cadena.

    """
    return NotNullValidator(
        next_validator=EventTypeValidator(next_validator=ProductDetailsValidator())
    )


def main() -> None:
    """
    Punto de entrada del validador de eventos.

    Recorre los eventos de prueba, los transforma usando `EventFactory`
    y los valida con la cadena de validadores. Imprime en consola el resultado
    de cada validación, indicando si fue exitosa o si se produjo un error.

    """
    validator_chain = build_validator_chain()

    for idx, raw_event in enumerate(test_events, start=1):
        print(f'\n🔹 Evento #{idx}:')
        try:
            event = EventFactory.create_event(raw_event)
            validator_chain.validate(event)
            print(MensajesGenerales.evento_valido.format(evento=event.to_dict()))
        except ValidationError as e:
            print(MensajesGenerales.evento_invalido.format(mensaje=e.message))
        except Exception as ex:
            print(MensajesGenerales.error_inesperado.format(error=str(ex)))


if __name__ == '__main__':
    main()
