def filter_chars(s):
    to_remove = set(s[318:337])
    to_remove = {char for char in to_remove if 'B' < char < 'z'}
    return ''.join((char for char in s if char not in to_remove))