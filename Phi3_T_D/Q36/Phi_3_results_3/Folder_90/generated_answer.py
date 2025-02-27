def filter_chars(s):
    to_remove = [c for c in s[344:len(s) - 874] if 'f' < c < '~']
    for char in to_remove:
        s = s.replace(char, '')
    return s