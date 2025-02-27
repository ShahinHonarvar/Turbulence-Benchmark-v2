def filter_chars(s):
    to_remove = set(s[28:66]).intersection({c for c in s if 'O' <= c <= 'd'})
    return ''.join((c for c in s if c not in to_remove))