def insert_after_character(string: str) -> str:
    return ''.join([c if c != 'O' else 'Od' for c in string])