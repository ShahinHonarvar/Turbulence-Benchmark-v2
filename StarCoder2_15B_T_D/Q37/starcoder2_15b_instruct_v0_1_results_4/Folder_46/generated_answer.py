def filter_chars(string):
    chars_to_remove = set(string[11:73]) - set('ijklm')
    return ''.join((c for c in string if c not in chars_to_remove))