def insert_before_character(string: str) -> str:
    result = ''
    for char in string:
        if char == 'e':
            result += 'Ee'
        else:
            result += char
    return result