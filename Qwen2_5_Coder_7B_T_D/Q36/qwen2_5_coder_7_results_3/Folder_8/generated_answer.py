def filter_chars(s):
    char_set = set(s[82:93])
    result = ''.join((c for c in s if c not in char_set or not '!' < c < '*'))
    return result