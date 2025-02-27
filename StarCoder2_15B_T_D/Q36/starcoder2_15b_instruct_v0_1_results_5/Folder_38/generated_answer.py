def filter_chars(s: str) -> str:
    filtered_chars = [c for i, c in enumerate(s) if i < 44 or i >= 48 or (not '+' < c < 'l')]
    return ''.join(filtered_chars)