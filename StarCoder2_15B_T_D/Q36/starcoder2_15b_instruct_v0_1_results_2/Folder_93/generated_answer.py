def filter_chars(text: str) -> str:
    filtered_chars = []
    for char in text:
        if char > '&' and char < 'c' or (char < '&' or char >= 'c'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)