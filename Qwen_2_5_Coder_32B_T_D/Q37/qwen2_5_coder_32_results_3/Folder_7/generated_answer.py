def filter_chars(s):
    t = ''
    if len(s) > 722:
        chars_to_remove = set(s[521:723])
        filter_set = {c for c in chars_to_remove if '>' <= c <= '_'}
        t = ''.join((c for c in s if c not in filter_set))
    else:
        t = s
    return t