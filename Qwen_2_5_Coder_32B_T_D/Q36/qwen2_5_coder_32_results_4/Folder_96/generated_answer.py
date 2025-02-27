def filter_chars(s):
    c = set(s[38:81])
    f = {x for x in c if '.' < x < '^'}
    return ''.join((x for x in s if x not in f))