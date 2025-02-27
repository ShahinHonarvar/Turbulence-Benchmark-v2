def filter_chars(s):
    to_remove = set(s[32:61])
    to_remove = {char for char in to_remove if '3' < char < 'D'}
    return ''.join((char for char in s if char not in to_remove))