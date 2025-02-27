def filter_chars(string: str) -> str:
    filtered_chars = []
    for char in string:
        if not (29 <= ord(char) <= 79 and ord('K') <= ord(char) <= ord('z')):
            filtered_chars.append(char)
    return ''.join(filtered_chars)