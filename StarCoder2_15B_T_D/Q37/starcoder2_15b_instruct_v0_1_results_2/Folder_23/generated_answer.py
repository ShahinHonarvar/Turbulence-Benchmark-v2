def filter_chars(text: str) -> str:
    filtered_chars = []
    for i, char in enumerate(text):
        if not (51 <= i <= 77 and 'V' <= char <= 'Y'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)