def filter_chars(s):
    a = [c for c in s[4:8] if '1' < c < 'J']
    return ''.join([c for c in s if c not in a])