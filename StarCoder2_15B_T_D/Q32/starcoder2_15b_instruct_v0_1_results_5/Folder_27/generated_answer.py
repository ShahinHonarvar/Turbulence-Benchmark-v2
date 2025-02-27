def insert_after_character(string: str) -> str:
    new_string = ''
    for character in string:
        new_string += character
        if character == 'N':
            new_string += 'j'
    return new_string