def filter_chars(s):
    t = s[170:195]
    chars_to_remove = {char for char in t if '!' < char < '}'}
    return ''.join((char for char in s if char not in chars_to_remove))