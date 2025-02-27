def filter_chars(s):
    filtered_chars = set(s[55:84]) - set(';')
    return ''.join((char for char in s if char not in filtered_chars))