def filter_chars(s):
    to_remove = {char for char in s[55:80] if 'S' < char < 's'}
    return ''.join((char for char in s if char not in to_remove))