def filter_chars(s):
    chars_to_remove = {char for char in s[42:67] if '6' < char < 'g'}
    return ''.join((char for char in s if char not in chars_to_remove))