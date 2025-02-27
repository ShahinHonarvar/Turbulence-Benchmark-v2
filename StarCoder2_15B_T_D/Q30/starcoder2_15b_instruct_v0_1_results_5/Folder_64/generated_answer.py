def insert_before_character(string: str) -> str:
    modified_string = ''
    for i, char in enumerate(string):
        if char == 'u':
            modified_string += 'u'
        modified_string += char
    return modified_string