def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if i < 35 or i >= 60 or (not '!' < char < 'B')]
    return ''.join(filtered_chars)