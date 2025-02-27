def filter_chars(s):
    remove_chars = set(s[318:337]) & set([chr(i) for i in range(ord('C'), ord('z'))])
    return ''.join((c for c in s if c not in remove_chars))