def filter_chars(s):
    remove_chars = set(s[15:56]) & set(map(chr, range(ord('W'), ord('{') + 1)))
    return ''.join((c for c in s if c not in remove_chars))