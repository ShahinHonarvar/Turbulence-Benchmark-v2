def filter_chars(string: str) -> str:
    filtered_chars = []
    for i, c in enumerate(string):
        if i < 225 or i > 381 or c < 'D' or (c > 'Y'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)