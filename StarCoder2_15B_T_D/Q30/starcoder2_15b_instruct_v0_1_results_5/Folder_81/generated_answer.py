def insert_before_character(string: str) -> str:
    return ''.join([char for char in string if char != 'A']) + 'A'