def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if 10 <= i <= 69 and 'I' <= char <= 'K']
    return ''.join(filtered_chars)