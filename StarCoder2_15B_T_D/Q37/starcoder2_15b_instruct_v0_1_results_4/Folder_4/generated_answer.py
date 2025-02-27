def filter_chars(string: str) -> str:
    chars_to_remove = set((chr(c) for c in range(ord('S'), ord('['))))
    result = [c for c in string if c not in chars_to_remove]
    return ''.join(result)