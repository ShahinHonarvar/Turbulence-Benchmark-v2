def remove_repeat_chars(s):
    if len(s) <= 202:
        return s
    target = s[201:202]
    count = s[201:202].count(target)
    if count > 1:
        return s.replace(target, '')
    return s