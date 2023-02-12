from typing import Dict, List, Any
import random
import uuid
from faker import Faker
import json

from common.common import (
    get_user_name,
    get_date_from_string,
    get_created_and_modified_at
)

from datagen import get_client_data


def get_user_data(client_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get a random client data as a dictionary
    
    Returns:
        Dict[str, Any]: Dictionary with client data
    """
    fake = Faker(locale="es_ES")

    user_data: Dict[str, Any] = {
        "user_id": uuid.uuid4().hex.upper(),
        "customer_id": client_data["customer_id"],
        "user_name": get_user_name(client_data["first_name"], client_data["last_name"]),
        "user_password": fake.password(length=random.randint(8, 16), special_chars=True, digits=True, upper_case=True, lower_case=True),
        "user_email": client_data["customer_email"],
        "user_phone": client_data["customer_phone"],
        "user_image_url": fake.image_url(),
        "url": fake.url(),
        "user_created_at": client_data["customer_created_at"],
        "user_updated_at": get_created_and_modified_at(fake, get_date_from_string(client_data["customer_created_at"]))[-1]
    }

    return user_data


if __name__ == "__main__":
    # Test module functionality by printing a random user data
    client_data: Dict[str, Any] = get_client_data()
    user_data: Dict[str, Any] = get_user_data(client_data)
    print(json.dumps(user_data, indent=4))
