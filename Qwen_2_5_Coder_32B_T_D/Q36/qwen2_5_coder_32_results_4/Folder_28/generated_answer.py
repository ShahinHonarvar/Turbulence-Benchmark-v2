def filter_chars(s):
    to_remove = set(s[31:73])
    to_remove = {char for char in to_remove if 'M' < char < 'j'}
    return ''.join((char for char in s if char not in to_remove))