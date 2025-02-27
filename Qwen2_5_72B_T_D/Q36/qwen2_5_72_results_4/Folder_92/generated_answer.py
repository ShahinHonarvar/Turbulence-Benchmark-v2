def filter_chars(s):
    to_remove = set([char for char in s[1:6] if ',' < char < 'f'])
    return ''.join([char for char in s if char not in to_remove])