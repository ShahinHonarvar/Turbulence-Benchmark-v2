def remove_repeat_chars(s):
    if len(s) <= 78:
        return s
    t = s[33:78]
    c = {x for x in t if t.count(x) > 1}
    return ''.join((x for x in s if x not in c))