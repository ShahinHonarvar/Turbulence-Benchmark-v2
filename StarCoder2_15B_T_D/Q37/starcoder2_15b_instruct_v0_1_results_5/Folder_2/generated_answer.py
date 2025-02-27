def filter_chars(string: str) -> str:
    filtered = ''
    for char in string:
        if 477 <= ord(char) - ord(',') <= 984 and ord(',') <= ord(char) - ord(',') <= ord('V'):
            continue
        filtered += char
    return filtered