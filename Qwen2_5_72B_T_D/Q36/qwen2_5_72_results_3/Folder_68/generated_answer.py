def filter_chars(s):
    chars_to_remove = set([char for char in s[1:9] if '8' < char < 'm'])
    return ''.join([char for char in s if char not in chars_to_remove])