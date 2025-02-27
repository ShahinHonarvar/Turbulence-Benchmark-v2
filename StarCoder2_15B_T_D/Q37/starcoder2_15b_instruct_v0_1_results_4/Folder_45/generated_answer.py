def filter_chars(s: str) -> str:
    filtered = [c for i, c in enumerate(s) if i < 72 or i > 94 or c < '.' or (c > 'b')]
    return ''.join(filtered)