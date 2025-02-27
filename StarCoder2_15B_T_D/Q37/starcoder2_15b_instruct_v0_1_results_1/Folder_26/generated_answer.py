def filter_chars(string):
    filtered_chars = [char for i, char in enumerate(string) if not (20 <= i <= 62 and 'i' <= char <= 'k')]
    return ''.join(filtered_chars)