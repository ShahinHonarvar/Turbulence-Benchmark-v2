def filter_chars(string: str) -> str:
    filtered_chars = []
    for char in string:
        if char >= 'm' and char <= 'w' or (char < 'a' or char > 'z'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)