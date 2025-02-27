def filter_chars(string: str) -> str:
    filtered_chars = [char for i, char in enumerate(string) if i < 81 or i >= 86 or (not '!' < char < 's')]
    return ''.join(filtered_chars)