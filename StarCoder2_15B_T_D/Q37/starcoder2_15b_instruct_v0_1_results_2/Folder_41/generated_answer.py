def filter_chars(string: str) -> str:
    filtered_chars = []
    for char in string:
        if not 26 <= ord(char) - ord('A') <= 64 or not 'V' <= char <= 'o':
            filtered_chars.append(char)
    return ''.join(filtered_chars)