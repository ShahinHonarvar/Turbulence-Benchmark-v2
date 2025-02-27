def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if i < 27 or i > 85 or char < 'c' or (char > 'i')]
    return ''.join(filtered_chars)