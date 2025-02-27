def remove_repeat_chars(s):
    if len(s) < 503:
        return s
    a = s[410:502]
    c = {ch for ch in a if a.count(ch) > 1}
    return ''.join((ch for ch in s if ch not in c))