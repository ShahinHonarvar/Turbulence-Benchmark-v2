def filter_chars(string: str) -> str:
    result = []
    for char in string:
        if char < 'w' or char > '{':
            result.append(char)
    return ''.join(result)