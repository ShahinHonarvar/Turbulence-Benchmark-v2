def insert_before_character(string: str) -> str:
    result = []
    for character in string:
        result.append(character)
        if character == 'k':
            result.append('k')
    return ''.join(result)