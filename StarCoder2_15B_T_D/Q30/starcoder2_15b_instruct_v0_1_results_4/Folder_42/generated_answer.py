def insert_before_character(string: str) -> str:
    result = ''
    for char in string:
        if char == 'O':
            result += 'jO'
        else:
            result += char
    return result