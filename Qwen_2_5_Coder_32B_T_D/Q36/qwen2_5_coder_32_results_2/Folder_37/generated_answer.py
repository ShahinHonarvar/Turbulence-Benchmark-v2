def filter_chars(s):
    t = s[44:59]
    chars_to_remove = {char for char in t if '/' < char < '6'}
    return ''.join((char for char in s if char not in chars_to_remove))