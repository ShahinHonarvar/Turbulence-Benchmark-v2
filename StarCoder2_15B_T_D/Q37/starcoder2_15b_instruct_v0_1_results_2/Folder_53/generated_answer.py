def filter_chars(s: str) -> str:
    filtered = [c for c in s if c < '*' or c > 'j' or s.index(c) < 83 or (s.index(c) > 99)]
    return ''.join(filtered)