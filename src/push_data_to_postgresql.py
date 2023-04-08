
from typing import List, Tuple, Dict, Any
import json
import requests
import psycopg2
from contextlib import closing
import time
import random
import logging

# configure logging
logging.basicConfig(
    level=logging.NOTSET,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("log_insert_data.log"),
        logging.StreamHandler()
    ]
)

def run_insert_query(query: str, connection: psycopg2.extensions.connection) -> None:
    try:
        cursor: psycopg2.extensions.cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        cursor.close()
    except Exception as e:
        logging.error(f"Error: {e}")
        logging.error(f"Query: {query}")
        connection.rollback()


def get_sql_statements(
    client_data: Dict[str, Any],
    user_data: Dict[str, Any],
    product_data: Dict[str, Any],
    category_data: Dict[str, Any],
    order_data: Dict[str, Any],
    invoice_data: Dict[str, Any]
    ) -> Tuple[str, str, str, str, str, str]:
    client_columns: str = ", ".join([col for col, _ in client_data.items()])
    client_values: str = ", ".join([f"'{str(value)}'" for _, value in client_data.items()])
    SQL_CLIENTS: str = f"INSERT INTO gcp_poc.onpremise.clients ({client_columns}) VALUES ({client_values});".replace("''", "NULL")

    user_columns: str = ", ".join([col for col, _ in user_data.items()])
    user_values: str = ", ".join([f"'{str(value)}'" for _, value in user_data.items()])
    SQL_USERS: str = f"INSERT INTO gcp_poc.onpremise.users ({user_columns}) VALUES ({user_values});".replace("''", "NULL")

    product_columns: str = ", ".join([col for col, _ in product_data.items()])
    product_values: str = ", ".join([f"""'{str(value).replace("'", "")}'""" for _, value in product_data.items()])
    SQL_PRODUCT: str = f"INSERT INTO gcp_poc.onpremise.products ({product_columns}) VALUES ({product_values});".replace("''", "NULL")

    categories_columns: str = ", ".join([col for col, _ in category_data.items()])
    categories_values: str = ", ".join([f"""'{str(value).replace("'", "")}'""" for _, value in category_data.items()])
    SQL_CATEGORIES: str = f"INSERT INTO gcp_poc.onpremise.categories ({categories_columns}) VALUES ({categories_values});".replace("''", "NULL")

    orders_columns: str = ", ".join([col for col, _ in order_data.items()])
    orders_values: str = ", ".join([f"""'{str(value).replace("'", "")}'""" for _, value in order_data.items()])
    SQL_ORDERS: str = f"INSERT INTO gcp_poc.onpremise.orders ({orders_columns}) VALUES ({orders_values});".replace("''", "NULL")

    invoice_columns: str = ", ".join([col for col, _ in invoice_data.items()])
    invoice_values: str = ", ".join([f"""'{str(value).replace("'", "")}'""" for _, value in invoice_data.items()])
    SQL_INVOICE: str = f"INSERT INTO gcp_poc.onpremise.invoices ({invoice_columns}) VALUES ({invoice_values});".replace("''", "NULL")
    
    return SQL_CLIENTS, SQL_USERS, SQL_PRODUCT, SQL_CATEGORIES, SQL_ORDERS, SQL_INVOICE

def run_insert_row():
    # db connection
    connection: psycopg2.extensions.connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="gcp_poc",
        user="fabio",
        password="fabio"
    )

    with closing(connection) as cn:
        random_rows_number: int = random.randrange(1, 50)
        endopoint = f"http://localhost:8000/get_{random_rows_number}_clients"
        response: requests.Response = requests.get(endopoint)
        logging.info(f"endpoint: {endopoint}")
        list_response_json: Dict[str, Any] = json.loads(response.text)
        
        for n, response_json in enumerate(list_response_json, start=1):
            logging.info(f"Inserting row {n} of {random_rows_number}")
            client_data: Dict[str, Any] = response_json.get("client_data")
            user_data: Dict[str, Any] = response_json.get("user_data")
            product_data: Dict[str, Any] = response_json.get("product_data")
            category_data: Dict[str, Any] = response_json.get("category_data")
            order_data: Dict[str, Any] = response_json.get("order_data")
            invoice_data: Dict[str, Any] = response_json.get("invoice_data")
            
            SQL_CLIENTS, SQL_USERS, SQL_PRODUCT, SQL_CATEGORIES, SQL_ORDERS, SQL_INVOICE = get_sql_statements(client_data, user_data, product_data, category_data, order_data, invoice_data)
            run_insert_query(SQL_CLIENTS, connection)
            run_insert_query(SQL_USERS, cn)
            run_insert_query(SQL_PRODUCT, cn)
            run_insert_query(SQL_CATEGORIES, cn)
            run_insert_query(SQL_ORDERS, cn)
            run_insert_query(SQL_INVOICE, cn)

if __name__ == "__main__":
    while True:
        seconds: int = random.randrange(1, 120)
        try:
            run_insert_row()
        except Exception as e:
            logging.error(f"Error: {e}")
        logging.info(f"Sleeping for {seconds} seconds")
        time.sleep(seconds)
