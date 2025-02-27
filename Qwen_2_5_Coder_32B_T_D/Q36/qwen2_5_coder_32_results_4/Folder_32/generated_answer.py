def filter_chars(s):
    chars_to_remove = set(s[40:63])
    chars_to_remove = {char for char in chars_to_remove if '7' < char < 'H'}
    return ''.join((char for char in s if char not in chars_to_remove))