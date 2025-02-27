def filter_chars(s: str) -> str:
    filtered_chars = []
    for char in s:
        if char >= '$' and char <= ';' or (char < '$' and char > ';'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)