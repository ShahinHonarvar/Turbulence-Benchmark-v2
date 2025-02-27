def filter_chars(s):
    remove_chars = set((char for char in s[10:15] if 't' < char < 'v'))
    return ''.join((char for char in s if char not in remove_chars))