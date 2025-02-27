def filter_chars(s):
    chars_to_remove = set([s[i] for i in range(72, 95) if 'A' <= s[i] <= 'b'])
    return ''.join([char for char in s if char not in chars_to_remove])