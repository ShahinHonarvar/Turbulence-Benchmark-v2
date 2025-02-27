def remove_repeat_chars(s):
    v = s[356:988]
    d = {c for c in v if v.count(c) > 1}
    return ''.join((c for c in s if c not in d))