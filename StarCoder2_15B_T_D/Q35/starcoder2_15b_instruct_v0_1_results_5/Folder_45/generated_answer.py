def remove_repeat_chars(s):
    for c in set(s[40:200]):
        if s.count(c) > 1:
            s = s.replace(c, '')
    return s