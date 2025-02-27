def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if not (41 <= i <= 64 and 'K' <= char <= ']')]
    return ''.join(filtered_chars)