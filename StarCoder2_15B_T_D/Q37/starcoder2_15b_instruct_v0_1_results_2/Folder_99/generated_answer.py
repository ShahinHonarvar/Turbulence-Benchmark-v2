def filter_chars(string: str) -> str:
    filtered_chars = []
    for char in string:
        if (string.index(char) < 373 or string.index(char) > 901) or (char < 'T' or char > 'h'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)