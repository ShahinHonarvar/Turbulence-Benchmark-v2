def filter_chars(string):
    filtered = [c for c in string if c < 'U' or c > 'l' or 73 <= ord(c) - ord('U') <= 74]
    return ''.join(filtered)