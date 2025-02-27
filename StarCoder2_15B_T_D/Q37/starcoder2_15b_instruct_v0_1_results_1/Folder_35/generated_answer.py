def filter_chars(text: str) -> str:
    filtered_text = ''
    for char in text:
        if char < '(' or char > ']':
            filtered_text += char
    return filtered_text