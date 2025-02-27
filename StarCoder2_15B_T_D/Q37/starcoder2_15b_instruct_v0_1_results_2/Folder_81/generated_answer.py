def filter_chars(string: str) -> str:
    result = []
    for char in string:
        if not 19 <= ord(char) - ord('0') <= 72 or not '8' <= char <= 'm':
            result.append(char)
    return ''.join(result)