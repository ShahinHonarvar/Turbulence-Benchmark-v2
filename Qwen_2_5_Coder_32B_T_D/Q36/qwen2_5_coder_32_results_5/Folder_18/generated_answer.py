def filter_chars(s):
    to_remove = set(s[587:648])
    filtered_set = {char for char in to_remove if ',' < char < 'c'}
    return ''.join((char for char in s if char not in filtered_set))