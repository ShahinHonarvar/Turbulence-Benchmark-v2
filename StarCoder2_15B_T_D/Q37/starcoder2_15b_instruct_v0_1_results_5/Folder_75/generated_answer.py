def filter_chars(string: str) -> str:
    result = []
    for index, character in enumerate(string):
        if 34 <= index <= 67 and 'W' <= character <= 'x':
            continue
        result.append(character)
    return ''.join(result)