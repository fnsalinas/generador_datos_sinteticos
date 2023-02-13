
from typing import List, Dict, Any
import json
from pathlib import Path


def get_hostname() -> str:
    """
    Get the hostname of the machine
    Returns:
        _type_: Hostname of the machine
    """

    with open("/etc/hostname", "r") as input_file:
        HOSTNAME: str = input_file.read().strip()

    return HOSTNAME


def get_app_path():
    """
    Run the configuration of the app and return the path of the app
    Returns:
        _type_: Path of the app directory
    """

    APP_PATH = Path(__file__).resolve()

    MAIN_PATH: List[str] = []
    for x in str(APP_PATH).split("/"):
        MAIN_PATH.append(x)
        if x == "generador_datos_sinteticos":
            break

    MAIN_PATH: str = "/".join(MAIN_PATH)

    return MAIN_PATH


def update_config_json() -> Dict[str, Any]:
    """
    Update the config.json file with new configuration parameters
    Args:
        config_json (Dict[str, Any]): Dictionary with the current configuration
        new_config (Dict[str, Any]): Dictionary with the new configuration
    Returns:
        _type_: Dictionary with the updated configuration
    """

    HOSTNAME: str = get_hostname()
    APPPATH: str = get_app_path()
    IP: str = "127.0.0.1" if "ip-" in HOSTNAME else "localhost"
    PORT: str = 8000

    with open(f"{APPPATH}/data/config/config_app.json", "r") as input_file:
        config_json: Dict[str, Any] = json.load(input_file)

    config_json[HOSTNAME] = {
        "app_main_path": APPPATH,
        "ip": IP,
        "port": PORT
    }

    with open(f"{APPPATH}/data/config/config_app.json", "w") as output_file:
        json.dump(config_json, output_file, indent=4)

    return config_json[HOSTNAME]


if __name__ == "__main__":
    # Test module functionality by printing the hostname of the machine
    # print(get_hostname())
    # print(get_app_path())
    update_config_json()
