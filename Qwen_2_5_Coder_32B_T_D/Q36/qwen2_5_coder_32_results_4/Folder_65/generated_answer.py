def filter_chars(s):
    chars_to_remove = set(s[58:82])
    chars_to_remove = {char for char in chars_to_remove if 'F' < char < 'O'}
    return ''.join((char for char in s if char not in chars_to_remove))