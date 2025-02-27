def filter_chars(string: str) -> str:
    filtered_chars = [char for char in string if char < '-' or char > 'n' or (char < '2' or char > '9')]
    return ''.join(filtered_chars)