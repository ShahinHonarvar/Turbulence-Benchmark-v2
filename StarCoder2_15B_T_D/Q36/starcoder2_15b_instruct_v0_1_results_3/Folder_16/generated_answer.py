def filter_chars(s: str) -> str:
    filtered = [c for c in s if c <= 'M' or c >= '_']
    return ''.join(filtered)