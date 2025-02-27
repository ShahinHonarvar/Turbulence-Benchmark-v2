def filter_chars(string: str) -> str:
    filtered_chars = [char for char in string if char < 'H' or char > 'e' or 38 <= string.index(char) <= 69]
    return ''.join(filtered_chars)