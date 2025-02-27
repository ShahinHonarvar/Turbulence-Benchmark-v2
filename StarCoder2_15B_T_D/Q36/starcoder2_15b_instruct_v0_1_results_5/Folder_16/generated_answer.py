def filter_chars(text: str) -> str:
    filtered_chars = []
    for index, char in enumerate(text):
        if index < 331 or index >= 713 or (not (char > 'M' and char < '_')):
            filtered_chars.append(char)
    filtered_text = ''.join(filtered_chars)
    return filtered_text