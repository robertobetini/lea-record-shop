import re

def email_is_valid(email: str) -> bool:
    email_pattern = "[\\w\\d\\.]+@[\\w\\d]+(?:\\.[\\w\\d]+)+$"
    return re.match(email_pattern, email) is not None
