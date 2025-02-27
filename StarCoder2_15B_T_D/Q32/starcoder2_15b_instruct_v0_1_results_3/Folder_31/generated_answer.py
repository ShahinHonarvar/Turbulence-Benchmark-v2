def insert_after_character(string: str) -> str:
    return ''.join([c if c != 'B' else 'NB' for c in string])