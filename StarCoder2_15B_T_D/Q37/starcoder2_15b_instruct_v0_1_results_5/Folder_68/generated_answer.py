def filter_chars(text: str) -> str:
    filtered_chars = []
    for char in text:
        if char < '6' or char > 'w' or (char < text[7] or char > text[9]):
            filtered_chars.append(char)
    return ''.join(filtered_chars)