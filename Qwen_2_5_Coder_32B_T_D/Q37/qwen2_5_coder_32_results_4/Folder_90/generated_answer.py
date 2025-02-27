def filter_chars(s):
    if len(s) < 853:
        return s
    chars_to_remove = set(s[348:853]) & set(range(ord('J'), ord('b') + 1))
    return ''.join((c for c in s if ord(c) not in chars_to_remove))