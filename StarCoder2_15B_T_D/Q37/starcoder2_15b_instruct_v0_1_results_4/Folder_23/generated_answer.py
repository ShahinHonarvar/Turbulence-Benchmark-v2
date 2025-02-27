def filter_chars(string: str) -> str:
    filtered_chars = [char for i, char in enumerate(string) if i < 51 or i > 77 or char < 'V' or (char > 'Y')]
    return ''.join(filtered_chars)