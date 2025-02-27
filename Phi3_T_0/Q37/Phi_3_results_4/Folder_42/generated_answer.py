def filter_chars(s):
    char_to_remove = s[73:75]
    filtered_string = ''.join([c for c in s if c not in char_to_remove])
    return filtered_string