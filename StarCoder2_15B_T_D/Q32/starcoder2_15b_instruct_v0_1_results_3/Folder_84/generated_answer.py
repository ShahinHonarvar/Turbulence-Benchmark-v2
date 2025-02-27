def insert_after_character(string: str) -> str:
    new_string = ''
    for i, c in enumerate(string):
        new_string += c
        if c == 'H':
            new_string += 'n'
    return new_string