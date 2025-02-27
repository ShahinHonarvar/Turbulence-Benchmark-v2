def filter_chars(s):
    filtered = [char for i, char in enumerate(s) if not (10 <= i <= 52 and '@' <= char <= 'T')]
    return ''.join(filtered)