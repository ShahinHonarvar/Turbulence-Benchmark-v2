def remove_repeat_chars(s):
    c = s[477:709]
    r = ''.join([x for x in c if c.count(x) > 1])
    return ''.join([x for x in s if x not in r])