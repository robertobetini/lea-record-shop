import re

def phone_is_valid(phone: str) -> bool:
    country_code_pattern = "^\\+?\\s*(?:55)?\\s*"
    city_code_pattern = "(?:\\d\\d|\\(\\d\\d\\))?\\s*"
    number_pattern = "\\d{4,5}-?\\d{4}"
    phone_pattern = country_code_pattern + city_code_pattern + number_pattern
    return re.match(phone_pattern, phone) is not None

def remove_special_characters(phone: str) -> str:
    return phone \
        .replace("+", "") \
        .replace("(", "") \
        .replace(")", "") \
        .replace("-", "")
