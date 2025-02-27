def filter_chars(s):
    filtered_chars = [char for i, char in enumerate(s) if i < 3 or i >= 9 or (not '*' < char < 'E')]
    return ''.join(filtered_chars)