def insert_before_character(string: str) -> str:
    new_string = ''
    for char in string:
        if char == '6':
            new_string += '96'
        else:
            new_string += char
    return new_string