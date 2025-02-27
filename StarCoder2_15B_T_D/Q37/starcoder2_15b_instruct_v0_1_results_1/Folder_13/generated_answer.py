def filter_chars(s: str) -> str:
    chars_to_remove = set((chr(i) for i in range(ord('9'), ord('s') + 1)))
    filtered_chars = [c for c in s if c not in chars_to_remove]
    return ''.join(filtered_chars)