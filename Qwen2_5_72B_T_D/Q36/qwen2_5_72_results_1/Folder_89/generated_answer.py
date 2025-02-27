def filter_chars(s):
    to_remove = set([char for char in s[57:69] if '(' < char < 'W'])
    return ''.join([char for char in s if char not in to_remove])