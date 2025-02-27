def filter_chars(text: str) -> str:
    filtered = ''
    for char in text:
        if char >= 'A' and char <= 'U':
            if text.index(char) < 52 or text.index(char) > 81:
                filtered += char
        else:
            filtered += char
    return filtered