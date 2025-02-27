def filter_chars(s):
    to_remove = set([char for char in s[3:8] if '?>' < char < 'k'])
    return ''.join([char for char in s if char not in to_remove])