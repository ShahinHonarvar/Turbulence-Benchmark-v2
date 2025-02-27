def filter_chars(string: str) -> str:
    filtered_chars = [char for char in string if char < 'K' or char > 'a' or (string.index(char) < 71 and string.index(char) > 94)]
    return ''.join(filtered_chars)