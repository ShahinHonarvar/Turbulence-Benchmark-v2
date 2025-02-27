def filter_chars(string: str) -> str:
    filtered_chars = []
    for char in string:
        if not 19 <= ord(char) - ord('f') <= 13:
            filtered_chars.append(char)
    return ''.join(filtered_chars)