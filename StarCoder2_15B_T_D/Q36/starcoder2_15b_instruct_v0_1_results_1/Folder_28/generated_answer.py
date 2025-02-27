def filter_chars(string: str) -> str:
    filtered = [char for char in string if 31 <= ord(char) < ord('M') or ord('j') <= ord(char) < 73]
    return ''.join(filtered)