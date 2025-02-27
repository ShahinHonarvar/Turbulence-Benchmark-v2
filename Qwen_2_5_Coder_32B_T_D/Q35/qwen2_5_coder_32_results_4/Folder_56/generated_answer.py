def remove_repeat_chars(s):
    if len(s) <= 9:
        return s
    target = s[8:9]
    count = target.count(s[8])
    if count > 1:
        return ''.join([char for char in s if char != s[8]])
    return s