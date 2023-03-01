import re

def is_valid_id(id_str):
    # Check if the string is a 12-byte hex string
    if re.match("^[0-9a-fA-F]{24}$", id_str):
        return True
    # Check if the string is a 24-character hex string
    if re.match("^[0-9a-fA-F]{12}$", id_str):
        return True
    return False
