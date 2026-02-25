import os
from tabnanny import verbose
from box.exceptions import BoxValueError
import yaml
import json
import joblib
from cnn_classification import logger

from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the yaml file.
    Returns:
        ConfigBox: ConfigBox object containing the yaml file data.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise BoxValueError(f"yaml file: {path_to_yaml} is empty")
    except Exception as e:
        raise e
    

def create_directories(path_to_directories: list[Path], verbose: bool = True) -> None:
    """
    Creates a list of directories.

    Args:
        path_to_directories (list[Path]): List of paths to the directories to be created.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
               

               logger.info(f"Directory: {path} created successfully")


def save_json(path: Path, data: dict) -> None:
    """
    Saves a dictionary as a json file.

    Args:
        path (Path): Path to the json file.
        data (dict): Dictionary to be saved as a json file.
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
        logger.info(f"json file: {path} saved successfully")


def load_json(path: Path) -> ConfigBox:
    """
    Loads a json file and returns a ConfigBox object.

    Args:
        path (Path): Path to the json file.
    Returns:
        ConfigBox: ConfigBox object containing the json file data.
    """
    with open(path) as json_file:
        content = json.load(json_file)
        logger.info(f"json file: {path} loaded successfully")
        return ConfigBox(content)

def save_bin(data: Any, path: Path) -> None:
    """
    Saves a binary file.

    Args:
        data (Any): Data to be saved as a binary file.
        path (Path): Path to the binary file.
    """
    joblib.dump(data, path)
    logger.info(f"binary file: {path} saved successfully")


def load_bin(path: Path) -> Any:
    """
    Loads a binary file.

    Args:
        path (Path): Path to the binary file.
    Returns:
        Any: Data loaded from the binary file.
    """
    data = joblib.load(path)
    logger.info(f"binary file: {path} loaded successfully")
    return data


def get_size(path: Path) -> str:
    """
    Returns the size of a file in KB.

    Args:
        path (Path): Path to the file.
    Returns:
        str: Size of the file in KB.
    """    
    size_in_kb = os.path.getsize(path) / 1024
    return f"{size_in_kb:.2f} KB"


def encode_image_to_base64(image_path: Path) -> str:
    """
    Encodes an image to a base64 string.

    Args:
        image_path (Path): Path to the image file.
    Returns:
        str: Base64 encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        logger.info(f"Image file: {image_path} encoded to base64 successfully")
        return encoded_string

def decode_base64_to_image(encoded_string: str, output_path: Path) -> None:
    """
    Decodes a base64 string to an image file.

    Args:
        encoded_string (str): Base64 encoded string of the image.
        output_path (Path): Path to save the decoded image file.
    """
    with open(output_path, "wb") as image_file:
        image_file.write(base64.b64decode(encoded_string))
        logger.info(f"Base64 string decoded to image file: {output_path} successfully")