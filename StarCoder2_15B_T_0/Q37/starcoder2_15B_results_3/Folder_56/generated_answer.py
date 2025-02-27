def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if i < 71 or i > 94 or char < 'K' or (char > 'a')]
    return ''.join(filtered_chars)