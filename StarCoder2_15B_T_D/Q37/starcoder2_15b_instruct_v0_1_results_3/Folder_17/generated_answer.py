def filter_chars(s: str) -> str:
    filtered_chars = []
    for char in s:
        if char < ';' or char > 'b':
            filtered_chars.append(char)
    return ''.join(filtered_chars)