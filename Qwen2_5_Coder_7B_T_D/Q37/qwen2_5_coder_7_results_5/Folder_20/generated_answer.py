def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('m'), ord('w') + 1)}
    return ''.join((c for c in s if c not in chars_to_remove or c not in {chr(i) for i in range(26, 100)}))