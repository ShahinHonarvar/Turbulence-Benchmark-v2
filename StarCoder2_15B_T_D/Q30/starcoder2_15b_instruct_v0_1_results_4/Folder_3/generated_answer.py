def insert_before_character(string: str) -> str:
    result = []
    for character in string:
        if character == '0':
            result.append('H')
        result.append(character)
    return ''.join(result)