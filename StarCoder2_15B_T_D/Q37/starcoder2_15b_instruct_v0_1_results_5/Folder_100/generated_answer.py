def filter_chars(string: str) -> str:
    filtered = [c for c in string if c < 'J' or c > 'Q' or string.index(c) < 88 or (string.index(c) > 90)]
    return ''.join(filtered)