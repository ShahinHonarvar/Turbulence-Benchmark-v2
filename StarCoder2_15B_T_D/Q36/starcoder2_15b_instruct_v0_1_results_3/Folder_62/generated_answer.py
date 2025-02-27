def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if i < 63 or i >= 89 or (not '*' < char < 'w')]
    return ''.join(filtered_chars)