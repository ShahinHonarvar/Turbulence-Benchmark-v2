def insert_before_character(string: str) -> str:
    new_string = ''
    for i, char in enumerate(string):
        if char == 'r':
            new_string += 'w'
        new_string += char
    return new_string