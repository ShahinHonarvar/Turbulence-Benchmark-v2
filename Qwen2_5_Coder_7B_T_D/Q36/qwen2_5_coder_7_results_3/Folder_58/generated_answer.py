def filter_chars(s):
    filtered_chars = [char for i, char in enumerate(s) if i < 318 or i >= 337 or (not 'B' < char < 'z')]
    return ''.join(filtered_chars)