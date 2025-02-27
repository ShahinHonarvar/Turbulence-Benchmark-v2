def filter_chars(s):
    if len(s) < 78:
        return s
    to_remove = set(s[42:78])
    to_remove = {char for char in to_remove if '!' < char < '?'}
    return ''.join((char for char in s if char not in to_remove))