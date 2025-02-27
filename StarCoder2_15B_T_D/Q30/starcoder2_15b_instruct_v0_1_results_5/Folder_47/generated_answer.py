def insert_before_character(string: str) -> str:
    result = ''
    for char in string:
        if char == 'E':
            result += 'fE'
        else:
            result += char
    return result