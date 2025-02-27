def filter_chars(s):
    chars_to_remove = set(s[2:10])
    chars_to_remove = {char for char in chars_to_remove if '8' < char < 'm'}
    return ''.join((char for char in s if char not in chars_to_remove))