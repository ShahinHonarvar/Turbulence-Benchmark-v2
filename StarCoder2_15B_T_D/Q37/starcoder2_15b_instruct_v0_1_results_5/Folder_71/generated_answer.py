def filter_chars(string: str) -> str:
    filtered_chars = []
    for char in string:
        if not (32 <= ord(char) <= 46 and '0' <= char <= 'k'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)