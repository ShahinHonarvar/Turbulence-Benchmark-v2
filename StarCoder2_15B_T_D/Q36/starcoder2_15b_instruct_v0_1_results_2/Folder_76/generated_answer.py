def filter_chars(text: str) -> str:
    filtered = [c for i, c in enumerate(text) if i < 669 or i >= 888 or c <= 'B' or (c >= 'Y')]
    return ''.join(filtered)