def filter_chars(string: str) -> str:
    filtered_chars = []
    for char in string:
        if not (37 <= ord(char) <= 56 and 54 <= ord(char) <= 95):
            filtered_chars.append(char)
    return ''.join(filtered_chars)