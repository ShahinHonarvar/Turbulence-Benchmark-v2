def filter_chars(s):
    char_to_remove = set((char for char in s[23:45] if '3' < char < 'I'))
    return ''.join((char for char in s if char not in char_to_remove))