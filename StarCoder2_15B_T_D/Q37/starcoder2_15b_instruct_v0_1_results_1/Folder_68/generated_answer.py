def filter_chars(s: str) -> str:
    char_range = range(ord('6'), ord('w') + 1)
    filtered_chars = [c for c in s if c not in char_range or s.index(c) < 7 or s.index(c) > 9]
    return ''.join(filtered_chars)