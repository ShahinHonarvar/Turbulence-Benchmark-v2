def filter_chars(s):
    chars = set(s[171:195])
    chars = {c for c in chars if '!' < c < '}'}
    return ''.join((c for c in s if c not in chars))