def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if i < 10 or i > 69 or char < 'I' or (char > 'K')]
    return ''.join(filtered_chars)