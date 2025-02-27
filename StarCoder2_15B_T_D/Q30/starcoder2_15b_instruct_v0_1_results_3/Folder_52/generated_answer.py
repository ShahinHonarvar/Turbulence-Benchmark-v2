def insert_before_character(string: str) -> str:
    return ''.join([c if c != 'T' else 'VT' for c in string])