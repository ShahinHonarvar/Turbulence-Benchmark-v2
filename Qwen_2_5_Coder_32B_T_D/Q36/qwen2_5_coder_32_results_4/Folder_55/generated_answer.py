def filter_chars(s):
    chars_to_remove = set(s[3:5])
    filtered_chars = [c for c in chars_to_remove if 'Y' < c < 's']
    result = ''.join([c for c in s if c not in filtered_chars])
    return result