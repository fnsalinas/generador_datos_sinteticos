
from typing import Dict, Any
import json

from datagen import (
    get_client_data,
    get_user_data,
    get_product_data,
    get_category_data,
    get_orders_data,
    get_invoice_data
)

# Test module functionality by printing a random user data
client_data: Dict[str, Any] = get_client_data()
user_data: Dict[str, Any] = get_user_data(client_data)
product_data: Dict[str, Any] = get_product_data()
category_data: Dict[str, Any] = get_category_data(product_data)
order_data: Dict[str, Any] = get_orders_data(client_data, product_data)
invoice_data: Dict[str, Any] = get_invoice_data(client_data, order_data)

FULL_DATA: Dict[str, Any] = {
    "client_data": client_data,
    "user_data": user_data,
    "product_data": product_data,
    "category_data": category_data,
    "order_data": order_data,
    "invoice_data": invoice_data
}

# print(json.dumps(FULL_DATA, indent=4))