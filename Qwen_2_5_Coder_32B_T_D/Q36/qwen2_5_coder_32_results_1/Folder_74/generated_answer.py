def filter_chars(s):
    chars_to_remove = set(s[34:36])
    filtered_chars = [char for char in s if char not in chars_to_remove or not '>' < char < 'A']
    return ''.join(filtered_chars)