def insert_before_character(string: str) -> str:
    return ''.join([c if c != 'E' else 'eE' for c in string])