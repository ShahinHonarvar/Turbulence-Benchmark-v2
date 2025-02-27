def insert_after_character(string: str) -> str:
    new_string = ''
    for index, character in enumerate(string):
        new_string += character
        if character == ' ':
            new_string += ' '
    return new_string