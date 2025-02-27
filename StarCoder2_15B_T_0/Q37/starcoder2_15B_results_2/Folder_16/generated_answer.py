def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if 225 <= i <= 381 and 'D' <= char <= 'Y']
    return ''.join(filtered_chars)