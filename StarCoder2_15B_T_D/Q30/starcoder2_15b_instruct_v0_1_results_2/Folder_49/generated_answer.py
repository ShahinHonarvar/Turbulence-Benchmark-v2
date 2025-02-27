def insert_before_character(string: str) -> str:
    result = ''
    for char in string:
        result += char
        if char == 'i':
            result += 'i'
    return result