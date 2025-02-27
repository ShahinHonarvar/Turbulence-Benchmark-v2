def filter_chars(s):
    chars_to_remove = set(s[58:81])
    chars_to_remove = {char for char in chars_to_remove if '5' < char < '>'}
    return ''.join((char for char in s if char not in chars_to_remove))