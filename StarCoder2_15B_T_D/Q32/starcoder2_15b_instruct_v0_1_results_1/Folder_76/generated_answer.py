def insert_after_character(string: str) -> str:
    new_string = ''
    for i, c in enumerate(string):
        if c == 'F':
            new_string += 'Fm'
        else:
            new_string += c
    return new_string