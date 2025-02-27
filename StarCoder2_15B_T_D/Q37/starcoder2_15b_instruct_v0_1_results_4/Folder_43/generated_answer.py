def filter_chars(s: str) -> str:
    filtered = [c for c in s if c < 'W' or c > '{' or s.index(c) < 15 or (s.index(c) > 55)]
    return ''.join(filtered)