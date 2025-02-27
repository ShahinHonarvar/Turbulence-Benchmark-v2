def filter_chars(text: str) -> str:
    return ''.join((c for i, c in enumerate(text) if not (58 < i < 81 and c > '5' and (c < '>'))))