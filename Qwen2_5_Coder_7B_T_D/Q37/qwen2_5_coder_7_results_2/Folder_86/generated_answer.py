def filter_chars(s):
    chars_to_remove = set(range(ord('O'), ord('}') + 1))
    return ''.join((c for i, c in enumerate(s) if not (164 <= i <= 706 and ord(c) in chars_to_remove)))