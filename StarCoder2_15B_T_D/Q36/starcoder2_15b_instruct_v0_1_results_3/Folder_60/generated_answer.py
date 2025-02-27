def filter_chars(string: str) -> str:
    filtered_chars = []
    for char in string:
        if char <= 'f' or char >= 'o':
            filtered_chars.append(char)
    return ''.join(filtered_chars)