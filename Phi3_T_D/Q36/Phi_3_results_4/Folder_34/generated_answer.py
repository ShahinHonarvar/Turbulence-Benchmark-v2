def filter_chars(s):
    filtered_chars = [char for i, char in enumerate(s) if not 10 <= i < 79 or '?' >= char or char >= 'm']
    return ''.join(filtered_chars)