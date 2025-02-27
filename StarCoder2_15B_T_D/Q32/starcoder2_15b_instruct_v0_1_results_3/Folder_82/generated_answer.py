def insert_after_character(string: str) -> str:
    return ''.join([c if c != 'I' else 'II' for c in string])