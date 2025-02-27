def filter_chars(s):
    if len(s) <= 636:
        return s
    chars_to_remove = set(s[171:636])
    chars_to_remove = {char for char in chars_to_remove if 'c' < char < 's'}
    return ''.join((char for char in s if char not in chars_to_remove))