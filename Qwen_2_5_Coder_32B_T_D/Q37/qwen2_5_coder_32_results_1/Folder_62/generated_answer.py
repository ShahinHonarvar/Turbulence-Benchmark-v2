def filter_chars(s):
    target_chars = set(s[10:70].intersection('IKJ'))
    return ''.join((c for c in s if c not in target_chars))