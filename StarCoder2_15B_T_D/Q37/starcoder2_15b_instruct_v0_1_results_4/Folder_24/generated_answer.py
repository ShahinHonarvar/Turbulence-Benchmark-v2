def filter_chars(string: str) -> str:
    filtered_chars = []
    for char in string:
        if char < '2' or char > 's' or (not 36 <= ord(char) <= 79):
            filtered_chars.append(char)
    return ''.join(filtered_chars)