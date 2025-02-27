def filter_chars(s):
    char_set = set(s[56:86])
    filtered_chars = [char for char in s if char not in char_set or char <= '+' or char >= 'w']
    return ''.join(filtered_chars)