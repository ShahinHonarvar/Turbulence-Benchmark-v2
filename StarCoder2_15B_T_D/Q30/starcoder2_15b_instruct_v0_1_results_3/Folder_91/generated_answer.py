def insert_before_character(string: str) -> str:
    result = ''
    for char in string:
        if char == 'a':
            result += '0a'
        else:
            result += char
    return result