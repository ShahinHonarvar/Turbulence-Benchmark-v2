def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('<') + 1, ord('C'))]
    chars_to_keep = [c for c in s if c not in chars_to_remove]
    return ''.join(chars_to_keep)