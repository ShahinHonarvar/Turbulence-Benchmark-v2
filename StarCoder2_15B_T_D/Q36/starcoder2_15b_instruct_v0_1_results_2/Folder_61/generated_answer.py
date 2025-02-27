def filter_chars(text: str) -> str:
    filtered_chars = []
    for char in text:
        if char < '*' or char > 'E':
            filtered_chars.append(char)
    return ''.join(filtered_chars)