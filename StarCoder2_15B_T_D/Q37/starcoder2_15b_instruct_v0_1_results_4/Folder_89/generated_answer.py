def filter_chars(s: str) -> str:
    char_range = range(ord('!'), ord('@') + 1)
    filtered_chars = [c for i, c in enumerate(s) if i < 11 or i > 32 or ord(c) not in char_range]
    return ''.join(filtered_chars)