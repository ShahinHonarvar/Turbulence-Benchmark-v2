def remove_repeat_chars(s):
    target = s[23:24]
    count = s[22:25].count(target)
    if count > 1:
        s = s.replace(target, '')
    return s