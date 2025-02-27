def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('*') + 1, ord('7'))}
    return ''.join([char for char in s if char not in chars_to_remove] if 219 < len(s) < 403 else s)