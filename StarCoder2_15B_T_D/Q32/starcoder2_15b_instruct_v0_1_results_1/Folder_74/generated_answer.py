def insert_after_character(string: str) -> str:
    return ''.join([c + '' if c == 'T' else c for c in string])