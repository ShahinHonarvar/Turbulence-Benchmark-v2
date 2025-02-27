def filter_chars(string: str) -> str:
    filtered = ''
    for char in string:
        if char < 'R' or char > 't':
            filtered += char
    return filtered