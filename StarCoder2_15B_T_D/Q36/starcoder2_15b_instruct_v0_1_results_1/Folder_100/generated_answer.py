def filter_chars(string: str) -> str:
    filtered_chars = [char for i, char in enumerate(string) if i < 43 or i >= 69 or char <= 'B' or (char >= 'r')]
    return ''.join(filtered_chars)