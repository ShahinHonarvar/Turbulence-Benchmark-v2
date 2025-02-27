def filter_chars(s):
    to_remove = {ch for ch in s[521:723] if '>' <= ch <= '_'}
    return ''.join((ch for ch in s if ch not in to_remove))