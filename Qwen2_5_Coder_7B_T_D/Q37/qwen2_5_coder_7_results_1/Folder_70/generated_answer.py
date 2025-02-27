def filter_chars(s):
    chars_to_remove = set(range(ord('+'), ord('}') + 1))
    return ''.join([c for c in s if not (515 <= s.index(c) <= 538 and ord(c) in chars_to_remove)])