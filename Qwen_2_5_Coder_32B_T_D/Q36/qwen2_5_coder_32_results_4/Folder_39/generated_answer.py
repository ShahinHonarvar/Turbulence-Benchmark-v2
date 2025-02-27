def filter_chars(s):
    to_remove = set(s[43:59])
    filtered = [char for char in s if char not in to_remove or not '5' < char < 'C']
    return ''.join(filtered)