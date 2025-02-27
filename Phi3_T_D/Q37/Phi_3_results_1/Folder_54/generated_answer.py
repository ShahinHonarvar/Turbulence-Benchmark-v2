def filter_chars(s):
    return ''.join([char for char in s if char not in s[46:86] or char < '-' or char > 'X'])