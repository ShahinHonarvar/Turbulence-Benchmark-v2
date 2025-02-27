def filter_chars(string):
    filtered_chars = [char for idx, char in enumerate(string) if idx < 513 or idx > 877 or char < '?' or (char > 'n')]
    return ''.join(filtered_chars)