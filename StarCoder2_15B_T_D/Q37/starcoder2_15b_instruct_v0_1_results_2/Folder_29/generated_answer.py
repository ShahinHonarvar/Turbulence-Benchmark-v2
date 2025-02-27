def filter_chars(s):
    chars_to_remove = set((chr(c) for c in range(ord('&'), ord('v') + 1)))
    result = [c for c in s if c not in chars_to_remove]
    return ''.join(result)