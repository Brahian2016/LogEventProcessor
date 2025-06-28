from models.product_view_event import ProductViewEvent
from models.add_to_cart_event import AddToCartEvent
from models.base_event import LogEvent


class EventFactory:
    @staticmethod
    def create_event(raw_data: dict) -> LogEvent:
        event_type = raw_data.get("event_type")

        if event_type == "view_product":
            return ProductViewEvent(
                event_type=raw_data["event_type"],
                user_id=raw_data["user_id"],
                timestamp=raw_data["timestamp"],
                product_id=raw_data["product_id"],
                product_name=raw_data["product_name"],
                device=raw_data.get("device"),
                app_version=raw_data.get("app_version"),
            )

        elif event_type == "add_to_cart":
            return AddToCartEvent(
                event_type=raw_data["event_type"],
                user_id=raw_data["user_id"],
                timestamp=raw_data["timestamp"],
                product_id=raw_data["product_id"],
                quantity=raw_data["quantity"],
                price=raw_data["price"],
                device=raw_data.get("device"),
                app_version=raw_data.get("app_version"),
            )

        else:
            # Aquí puedes lanzar una excepción o retornar un LogEvent genérico
            raise ValueError(f"Tipo de evento no soportado: {event_type}")
