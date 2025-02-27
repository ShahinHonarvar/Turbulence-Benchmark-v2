def remove_repeat_chars(s):
    a = s[45:91]
    d = {x for x in a if a.count(x) > 1}
    return ''.join((x for x in s if x not in d))