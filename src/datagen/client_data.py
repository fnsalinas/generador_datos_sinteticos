from typing import Dict, List, Any
import random
from io import StringIO
import uuid
from faker import Faker
import json
import pandas as pd

from common.common import (
    get_latlong,
    get_email,
    get_created_and_modified_at
)


def get_client_data() -> Dict[str, Any]:
    """
    Get a random client data as a dictionary
    
    Returns:
        Dict[str, Any]: Dictionary with client data
    """
    fake = Faker(locale="es_ES")

    BLOOD_TYPES = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    SEX: str = random.choice(["male", "female"])

    HEADER = ["nif", "first_name", "last_name", "date_of_birth", "city", "customer_address",
              "latlng", "region", "timezone", "customer_phone", "customer_email"]
    DATA_COLUMNS = ('{{nif}}', '{{first_name_SEX}}'.replace("SEX", SEX), '{{last_name_SEX}}'.replace("SEX", SEX),
                    '{{date_of_birth}}', '{{city}}', '{{address}}', '{{latlng}}', '{{region}}', '{{timezone}}',
                    '{{phone_number}}', '{{free_email}}')

    raw_data: str = fake.csv(
        header=HEADER,
        data_columns=DATA_COLUMNS,
        num_rows=1
    )

    df = pd.read_csv(StringIO(raw_data), sep=",", dtype=str)
    df["customer_id"] = uuid.uuid4().hex.upper()
    df["sex"] = SEX
    df["blood_group"] = random.choice(BLOOD_TYPES)

    lat, long = get_latlong(df.loc[0, "latlng"])
    df["lat"] = lat
    df["long"] = long
    df["customer_email"] = get_email(
        df.loc[0, "first_name"], df.loc[0, "last_name"], df.loc[0, "date_of_birth"])

    created_at, modified_at = get_created_and_modified_at(fake)
    df["customer_created_at"] = created_at
    df["customer_updated_at"] = modified_at

    cols: List[str] = ['customer_id', 'nif', 'first_name', 'last_name', 'date_of_birth',
                       'sex', 'blood_group', 'city', 'customer_address', 'lat', 'long',
                       'region', 'timezone', 'customer_phone', 'customer_email',
                       'customer_created_at', 'customer_updated_at']

    df = df[cols]

    client_data: Dict[str, Any] = df.T.to_dict()[0]

    return client_data


if __name__ == "__main__":
    # Test module functionality by printing a random client data
    client_data: Dict[str, Any] = get_client_data()
    print(json.dumps(client_data, indent=4))
