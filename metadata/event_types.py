"""
Define los tipos de eventos válidos que pueden ser procesados por el sistema.
Estos eventos representan acciones realizadas por los usuarios en la aplicación.
"""

from typing import List


class TipoEventosValidos:
    """
    Contiene constantes que representan los tipos de eventos válidos del sistema.

    Atributos:
        view_product: Evento cuando un usuario visualiza un producto.
        add_to_cart: Evento cuando un usuario agrega un producto al carrito.

        lista_tipo_eventos: Lista de todos los tipos de eventos válidos,
        utilizada para validaciones y control de flujo.

    """

    view_product: str = 'view_product'
    add_to_cart: str = 'add_to_cart'

    lista_tipo_eventos: List[str] = [view_product, add_to_cart]
