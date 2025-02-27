def insert_before_character(string: str) -> str:
    return ''.join([c if c != 'o' else 'O' for c in string])