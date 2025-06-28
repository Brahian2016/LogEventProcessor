"""
Define los campos específicos requeridos según el tipo de evento.
Esto permite realizar validaciones dinámicas dependiendo del evento recibido.
"""

from typing import Dict, List
from metadata.event_types import TipoEventosValidos


class CamposPorTipoEvento:
    """
    Contiene el mapeo entre cada tipo de evento y los campos específicos
    que deben estar presentes en los datos del evento.

    Atributos:
        campos_especificos: Diccionario donde la clave es
        el nombre del evento y el valor es la lista de campos requeridos para dicho evento.

    """

    product_id = 'product_id'
    product_name = 'product_name'
    quantity = 'quantity'
    price = 'price'

    campos_especificos: Dict[str, List[str]] = {
        TipoEventosValidos.view_product: [product_id, product_name],
        TipoEventosValidos.add_to_cart: [product_id, quantity, price],
    }
