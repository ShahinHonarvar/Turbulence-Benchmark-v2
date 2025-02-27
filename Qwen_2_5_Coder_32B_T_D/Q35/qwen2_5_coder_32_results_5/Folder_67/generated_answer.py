def remove_repeat_chars(s):
    if len(s) <= 67:
        return s
    a = s[44:67]
    r = {c for c in a if a.count(c) > 1}
    return ''.join([c for c in s if c not in r])