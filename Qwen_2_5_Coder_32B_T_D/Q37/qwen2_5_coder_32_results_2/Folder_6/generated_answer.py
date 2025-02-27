def filter_chars(s):
    a = set(s[13:29])
    b = {x for x in a if 'c' <= x <= 'n'}
    return ''.join([x for x in s if x not in b])