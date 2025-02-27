def filter_chars(s):
    to_remove = set(s[2:6])
    result = [char for char in s if char not in to_remove or not ',' < char < 'f']
    return ''.join(result)