def filter_chars(s):
    chars_to_remove = set([s[4]]) if 4 < len(s) and '7' <= s[4] <= 'o' else set()
    return ''.join([char for char in s if char not in chars_to_remove])