def insert_after_character(string: str) -> str:
    result = ''
    for char in string:
        if char == 'a':
            result += 'aW'
        else:
            result += char
    return result