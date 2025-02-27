def filter_chars(s):
    chars_to_remove = set(s[70:97])
    filtered_chars = {char for char in chars_to_remove if 'V' < char < 'j'}
    return ''.join((char for char in s if char not in filtered_chars))