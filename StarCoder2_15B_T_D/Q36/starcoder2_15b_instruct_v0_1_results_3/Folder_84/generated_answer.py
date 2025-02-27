def filter_chars(s: str) -> str:
    filtered = [c for c in s if not (171 < s.index(c) < 636 and c > 'c' and (c < 's'))]
    return ''.join(filtered)