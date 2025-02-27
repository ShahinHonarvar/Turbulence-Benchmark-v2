def insert_after_character(string: str) -> str:
    modified_string = ''
    for index, char in enumerate(string):
        modified_string += char
        if char == 'c':
            modified_string += 'G'
    return modified_string