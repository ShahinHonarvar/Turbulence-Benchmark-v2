def filter_chars(string):
    chars_to_remove = set((chr(i) for i in range(32, 47) if chr(i) >= '0' and chr(i) <= 'k'))
    return ''.join((c for c in string if c not in chars_to_remove))