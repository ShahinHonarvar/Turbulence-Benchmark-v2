def filter_chars(s):
    chars_to_remove = set([s[i] for i in range(19, min(len(s), 93)) if '8' <= s[i] <= 'm'])
    return ''.join([char for char in s if char not in chars_to_remove])