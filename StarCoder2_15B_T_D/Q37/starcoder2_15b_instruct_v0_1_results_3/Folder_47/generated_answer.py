def filter_chars(s: str) -> str:
    filtered_chars = [c for i, c in enumerate(s) if not (38 <= i <= 54 and ':' <= c <= 'r')]
    return ''.join(filtered_chars)