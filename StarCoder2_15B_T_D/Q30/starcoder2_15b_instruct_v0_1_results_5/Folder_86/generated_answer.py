def insert_before_character(string: str) -> str:
    return ''.join([c if c != 'O' else 'QO' for c in string])