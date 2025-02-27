def filter_chars(s):
    r = ''.join([c for c in s[3:8] if '?' < c < 'k'])
    return ''.join([x for x in s if x not in r])