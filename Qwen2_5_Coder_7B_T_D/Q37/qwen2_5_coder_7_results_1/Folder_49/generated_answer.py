def filter_chars(s):
    filter_set = set(range(ord('*'), ord('b') + 1))
    return ''.join((c for i, c in enumerate(s) if not (42 <= i <= 97 and ord(c) in filter_set)))