def filter_chars(s):
    to_remove = set(s[284:483])
    to_remove = {char for char in to_remove if 'l' < char < 't'}
    return ''.join((char for char in s if char not in to_remove))