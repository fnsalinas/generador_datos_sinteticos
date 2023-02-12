
from faker import Faker
from datetime import datetime
from typing import Tuple, List
import random


def get_latlong(latlng: str) -> Tuple[str, str]:
    """
    Get latitude and longitude from a string with format: 'lat, long'
    Args:
        latlng (str): String with format: 'lat, long'

    Returns:
        Tuple[str, str]: Latitude and longitude as strings
    """
    lat, long = latlng.split(",")
    lat, long = lat.split("'")[1], long.split("'")[1]
    return lat, long


def get_email(first_name: str, last_name: str, birth_date: str) -> str:
    """
    Get a random email from a first name, last name and birth date (format: YYYY-MM-DD)
    Args:
        first_name (str): First name of the person to generate the email
        last_name (str): Last name of the person to generate the email
        birth_date (str): Birth date of the person to generate the email (format: YYYY-MM-DD)

    Returns:
        str: Random email generated
    """
    t1 = "".join(random.choices(
        first_name, k=random.randint(3, len(first_name)))).lower()
    t2 = "".join(random.choices(
        last_name, k=random.randint(3, len(last_name)))).lower()
    t3 = "".join(random.choices(birth_date.replace("-", ""),
                 k=random.randint(3, len(birth_date.replace("-", ""))))).lower()

    EMAIL_DOMAINS: List[str] = ["gmail.com", "hotmail.com", "msn.com", "yahoo.com", "outlook.com", "live.com", "aol.com", "icloud.com", "mail.com",
                                "protonmail.com", "zoho.com", "yandex.com", "gmx.com", "mail.ru", "inbox.com", "tutanota.com", "hushmail.com", "gmx.net"]
    EMAIL_DOMAIN: str = random.choice(EMAIL_DOMAINS)

    return f"{t1}{t2}{random.choice(['-', '_', ''])}{t3}@{EMAIL_DOMAIN}".replace(" ", "")


def get_created_and_modified_at(fake: Faker, created_at_start_date: datetime = datetime(2015, 1, 1), force_generation_mod_date: bool = False) -> Tuple[str, str]:
    """
    Get a random created_at and modified_at date and time
    Returns:
        Tuple[str, str]: created_at and modified_at date and time as strings
    """
    created_at_dt: str = fake.date_time_between(
        start_date=created_at_start_date, end_date="now", tzinfo=None)
    created_at_str: str = f"{created_at_dt.strftime('%Y-%m-%d %H:%M:%S')} UTC"

    modified_at_dt: str = fake.date_time_between(
        start_date=created_at_dt, end_date="now", tzinfo=None)
    modified_at_str: str = f"{modified_at_dt.strftime('%Y-%m-%d %H:%M:%S')} UTC"
    if not force_generation_mod_date:
        modified_at_str: str = random.choice([modified_at_str, "", "", ""])

    return created_at_str, modified_at_str


def get_user_name(first_name: str, last_name: str) -> str:
    """
    Get a random user name from a first name and a last name as a string
    
    Args:
        first_name (str): First name
        last_name (str): Last name
    
    Returns:
        str: Random user name
    """
    random_number: str = f"{random.randint(1, 9999):04d}"
    user_name: str = f"{first_name.replace(' ', '_')}_{last_name.replace(' ', '_')}_{random_number}".lower(
    )
    user_name: str = "".join(
        [x for x in user_name if x.isalnum() or x in ['_', '-']])

    return user_name


def get_date_from_string(date_str: str) -> datetime:
    """
    Get a datetime object from a string with a date in the format YYYY-MM-DD as a datetime
    Args:
        date_str (str): Date in the format YYYY-MM-DD as a string

    Returns:
        datetime: Datetime object from a string with a date in the format YYYY-MM-DD
    """
    y, m, d = int(date_str[:4]), int(date_str[5:7]), int(date_str[8:10])
    return datetime(y, m, d)
