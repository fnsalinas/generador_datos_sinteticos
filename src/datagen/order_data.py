
from typing import Dict, List, Any
import random
import json
from faker import Faker
import uuid

from common.common import (
    get_user_name,
    get_date_from_string,
    get_created_and_modified_at
)
from datagen import get_client_data, get_user_data, get_product_data, get_category_data

from csv import DictReader

columns_orders: List[str] = ["order_id", "order_customer_id", "order_product_id",
                             "order_quantity", "order_price", "order_created_at", "order_updated_at"]


def get_orders_data(client_data: Dict[str, Any], product_data: Dict[str, Any]) -> Dict[str, Any]:

    fake = Faker(locale="es_ES")

    order_data: Dict[str, Any] = {
        "order_id": uuid.uuid4().hex.upper(),
        "order_customer_id": client_data["customer_id"],
        "order_product_id": product_data["product_id"],
        "order_quantity": random.randint(1, 10),
        "order_price": product_data["product_price"],
        "order_created_at": get_created_and_modified_at(fake, get_date_from_string(client_data["customer_created_at"]), True)[-1],
        "order_updated_at": ""
    }

    return order_data


if __name__ == "__main__":
    # Test module functionality by printing a random user data
    client_data: Dict[str, Any] = get_client_data()
    user_data: Dict[str, Any] = get_user_data(client_data)
    product_data: Dict[str, Any] = get_product_data()
    category_data: Dict[str, Any] = get_category_data(product_data)
    order_data: Dict[str, Any] = get_orders_data(client_data, product_data)
    print(json.dumps(order_data, indent=4))
