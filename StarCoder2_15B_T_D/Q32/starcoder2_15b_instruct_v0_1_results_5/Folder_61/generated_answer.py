def insert_after_character(string: str) -> str:
    new_string = ''
    for i, c in enumerate(string):
        if c == 'e':
            new_string += '0'
        new_string += c
    return new_string