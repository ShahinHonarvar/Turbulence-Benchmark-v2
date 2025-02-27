def filter_chars(text: str) -> str:
    filtered_chars = []
    for i, c in enumerate(text):
        if i < 155 or i > 403 or c < '(' or (c > ']'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)