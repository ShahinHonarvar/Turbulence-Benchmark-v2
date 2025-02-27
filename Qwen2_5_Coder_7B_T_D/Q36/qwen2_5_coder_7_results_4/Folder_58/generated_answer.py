def filter_chars(s):
    filter_set = set(range(ord('B') + 1, ord('z')))
    return ''.join((c for c in s if ord(c) not in filter_set))