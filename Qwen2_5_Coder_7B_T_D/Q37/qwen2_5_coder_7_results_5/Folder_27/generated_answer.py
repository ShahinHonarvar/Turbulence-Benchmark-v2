def filter_chars(s):
    chars_to_remove = set(range(ord('='), ord('F')))
    return ''.join((c for c in s if (ord(c) < 43 or ord(c) > 80) or ord(c) not in chars_to_remove))