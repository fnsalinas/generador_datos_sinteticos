
from typing import Dict, List, Any
import random
import json

from datagen import (
    get_client_data,
    get_user_data,
    get_product_data
)

from csv import DictReader


def get_categories_list() -> List[Dict[str, Any]]:
    categories_file_path: str = "/home/ubuntu/workspace/fsalinas/generador_datos_sinteticos/data/datasets/categories.csv"

    with open(categories_file_path, "r") as input_file:
        reader: DictReader = DictReader(input_file)
        categories: List[Dict[str, Any]] = list(reader)

    return categories


def get_category_data(product_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get a random product data as a dictionary from a list of products
    Returns:
        Dict[str, Any]: Dictionary with product data from a list of products
    """

    category_name: str = product_data["product_category"]
    categories_list: List[Dict[str, Any]] = get_categories_list()

    category: List[Dict[str, Any]] = [
        cat for cat in categories_list if cat["category_name"] == category_name]

    if len(category) == 0:
        category = [random.choice(categories_list)]

    return category[0]


if __name__ == "__main__":
    # Test module functionality by printing a random user data
    client_data: Dict[str, Any] = get_client_data()
    user_data: Dict[str, Any] = get_user_data(client_data)
    product_data: Dict[str, Any] = get_product_data()
    category_data: Dict[str, Any] = get_category_data(product_data)
    print(json.dumps(category_data, indent=4))
