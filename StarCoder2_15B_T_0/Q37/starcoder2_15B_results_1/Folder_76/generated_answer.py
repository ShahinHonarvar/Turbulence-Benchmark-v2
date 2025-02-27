def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if i < 379 or i > 898 or char < 'M' or (char > 'v')]
    return ''.join(filtered_chars)