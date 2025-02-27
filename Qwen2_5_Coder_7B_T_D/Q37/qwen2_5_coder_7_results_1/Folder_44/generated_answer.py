def filter_chars(s):
    chars_to_remove = set(range(ord('+'), ord('9') + 1))
    return ''.join((ch for ch in s if (ord(ch) < 21 or ord(ch) > 43) or ord(ch) not in chars_to_remove))