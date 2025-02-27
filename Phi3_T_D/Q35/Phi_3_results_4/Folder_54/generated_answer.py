def remove_repeat_chars(s):
    if len(s) < 35 or len(s) > 64:
        return s
    charset = set(s[35:64])
    return ''.join([c for c in s if c not in charset or s.count(c) <= 1])