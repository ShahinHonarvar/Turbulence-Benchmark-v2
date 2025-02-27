def filter_chars(s):
    to_remove = set((char for char in s[77:87] if ';' < char < 'r'))
    return ''.join((char for char in s if char not in to_remove))