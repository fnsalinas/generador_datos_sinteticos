
from typing import Dict, List, Any
import random
import json
from csv import DictReader

from datagen import get_client_data, get_user_data
from common.config_app import update_config_json

config: Dict[str, Any] = update_config_json()
APP_MAIN_PATH: str = config["app_main_path"]

def get_products_list() -> List[Dict[str, Any]]:
    product_file_path: str = f"{APP_MAIN_PATH}/data/datasets/products.csv"
    
    with open(product_file_path, "r") as input_file:
        reader: DictReader = DictReader(input_file)
        products: List[Dict[str, Any]] = list(reader)
    
    return products

def get_product_data() -> Dict[str, Any]:
    """
    Get a random product data as a dictionary from a list of products
    Returns:
        Dict[str, Any]: Dictionary with product data from a list of products
    """
    
    one_random_product: Dict[str, Any] = random.choice(get_products_list())

    return one_random_product


if __name__ == "__main__":
    # Test module functionality by printing a random user data
    client_data: Dict[str, Any] = get_client_data()
    user_data: Dict[str, Any] = get_user_data(client_data)
    product_data: Dict[str, Any] = get_product_data()
    print(json.dumps(product_data, indent=4))
