def filter_chars(s):
    to_remove = set((char for char in s[69:97] if 'V' < char < 'j'))
    return ''.join((char for char in s if char not in to_remove))