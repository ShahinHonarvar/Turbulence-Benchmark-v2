def filter_chars(s):
    chars_to_remove = set(s[54:92])
    chars_to_remove = {char for char in chars_to_remove if 'J' < char < 'X'}
    return ''.join((char for char in s if char not in chars_to_remove))