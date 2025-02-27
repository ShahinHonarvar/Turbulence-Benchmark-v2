def remove_repeat_chars(s):
    t = s[1:5]
    c = {x for x in t if t.count(x) > 1}
    return ''.join((x for x in s if x not in c))