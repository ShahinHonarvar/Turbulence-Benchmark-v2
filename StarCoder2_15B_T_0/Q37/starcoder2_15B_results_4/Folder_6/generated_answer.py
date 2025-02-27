def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if i < 13 or i > 28 or char < 'c' or (char > 'n')]
    return ''.join(filtered_chars)