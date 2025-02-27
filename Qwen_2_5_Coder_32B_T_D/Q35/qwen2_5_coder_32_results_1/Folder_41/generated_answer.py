def remove_repeat_chars(s):
    a = s[4:8]
    d = {c for c in a if a.count(c) > 1}
    return ''.join((c for c in s if c not in d))