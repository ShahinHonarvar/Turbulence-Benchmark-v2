def filter_chars(string: str) -> str:
    filtered_chars = [char for i, char in enumerate(string) if i < 770 or i > 970 or char < '-' or (char > 'D')]
    return ''.join(filtered_chars)