def insert_after_character(string: str) -> str:
    inserted_string = ''
    for character in string:
        inserted_string += character
        if character == '9':
            inserted_string += 'M'
    return inserted_string