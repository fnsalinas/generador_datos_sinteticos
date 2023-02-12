
from typing import Dict, Any
import json
from faker import Faker
import uuid

from datagen import get_client_data, get_user_data, get_product_data, get_category_data, get_orders_data
from common.common import (
    get_date_from_string,
    get_created_and_modified_at
)


def get_invoice_data(client_data: Dict[str, Any], order_data: Dict[str, Any]) -> Dict[str, Any]:

    fake = Faker(locale="es_ES")

    invoice_data: Dict[str, Any] = {
        "invoice_id": uuid.uuid4().hex.upper(),
        "invoice_customer_id": client_data["customer_id"],
        "invoice_order_id": order_data["order_id"],
        "invoice_amount": f"{float(order_data['order_price']) * int(order_data['order_quantity'])}",
        "invoice_created_at": get_created_and_modified_at(fake, get_date_from_string(client_data["customer_created_at"]), True)[-1],
        "invoice_updated_at": ""
    }

    return invoice_data


if __name__ == "__main__":
    # Test module functionality by printing a random user data
    client_data: Dict[str, Any] = get_client_data()
    user_data: Dict[str, Any] = get_user_data(client_data)
    product_data: Dict[str, Any] = get_product_data()
    category_data: Dict[str, Any] = get_category_data(product_data)
    order_data: Dict[str, Any] = get_orders_data(client_data, product_data)
    invoice_data: Dict[str, Any] = get_invoice_data(client_data, order_data)
    print(json.dumps(invoice_data, indent=4))
