def filter_chars(s):
    filter_chars = set(range(ord('/'), ord('9') + 1))
    return ''.join((c for c in s if 384 > ord(c) > 411 or ord(c) not in filter_chars))