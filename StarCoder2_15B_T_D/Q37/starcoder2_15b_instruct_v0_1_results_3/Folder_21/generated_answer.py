def filter_chars(string: str) -> str:
    filtered = []
    for char in string:
        if char < 'Q' or char > 'h':
            filtered.append(char)
    return ''.join(filtered)