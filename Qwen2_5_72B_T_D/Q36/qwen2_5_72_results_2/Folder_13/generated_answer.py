def filter_chars(s):
    to_remove = {c for c in s[323:526] if ')' < c < 'O'}
    return ''.join((c for c in s if c not in to_remove))