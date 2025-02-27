def insert_after_character(string: str) -> str:
    new_string = ''
    for char in string:
        new_string += char
        if char == 'e':
            new_string += '0'
    return new_string