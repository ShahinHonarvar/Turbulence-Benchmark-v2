def filter_chars(s: str) -> str:
    filtered = [c for c in s if c <= ';' or c >= 'r']
    return ''.join(filtered)