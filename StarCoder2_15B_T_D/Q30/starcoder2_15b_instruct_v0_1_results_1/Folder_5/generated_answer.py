def insert_before_character(string: str) -> str:
    new_string = ''
    for i, char in enumerate(string):
        if char == 'c':
            new_string += 'Gc'
        else:
            new_string += char
    return new_string