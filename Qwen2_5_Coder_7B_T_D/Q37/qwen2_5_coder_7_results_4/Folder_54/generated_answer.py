def filter_chars(s):
    chars_to_remove = set(range(ord('-'), ord('X') + 1))
    return ''.join((c for c in s if not (46 <= ord(c) <= 85 and ord(c) in chars_to_remove)))