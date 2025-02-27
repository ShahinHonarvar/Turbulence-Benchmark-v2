def filter_chars(s: str) -> str:
    filtered = [c for c in s if not (c > ':' and c < 'C')]
    return ''.join(filtered)