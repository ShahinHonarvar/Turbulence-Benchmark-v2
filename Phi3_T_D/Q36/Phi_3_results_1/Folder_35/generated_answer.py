def filter_chars(s):
    chars_to_remove = filter(lambda c: '(' < c < ']', s[163:658])
    filtered_string = ''.join([c for c in s if c not in chars_to_remove])
    return filtered_string