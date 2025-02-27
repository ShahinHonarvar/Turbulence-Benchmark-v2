def filter_chars(s: str) -> str:
    filtered_chars = [c for i, c in enumerate(s) if i < 669 or i >= 888 or c <= 'B' or (c >= 'Y')]
    return ''.join(filtered_chars)