def filter_chars(s):
    t = s[299:418]
    chars_to_remove = {char for char in t if '9' < char < 'P'}
    return ''.join((char for char in s if char not in chars_to_remove))