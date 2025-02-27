def filter_chars(s):
    result = [c for i, c in enumerate(s) if not (54 <= i <= 83 and 'j' <= c <= 'v')]
    return ''.join(result)