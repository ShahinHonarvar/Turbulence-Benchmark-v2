def filter_chars(s):
    chars_to_remove = set(s[66:90])
    filtered_chars = {char for char in chars_to_remove if '#' < char < 'T'}
    return ''.join((char for char in s if char not in filtered_chars))