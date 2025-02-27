def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if i < 24 or i > 79 or char < 'a' or (char > 'f')]
    return ''.join(filtered_chars)