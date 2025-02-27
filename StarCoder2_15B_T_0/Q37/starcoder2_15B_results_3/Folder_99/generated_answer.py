def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if i < 373 or i > 901 or char < 'T' or (char > 'h')]
    return ''.join(filtered_chars)