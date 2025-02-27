def filter_chars(s):
    set_remove = {c for c in s[521:723] if '>' <= c <= '_'}
    return ''.join((c for c in s if c not in set_remove))