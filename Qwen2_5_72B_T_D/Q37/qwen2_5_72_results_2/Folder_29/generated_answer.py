def filter_chars(s):
    chars_to_remove = set([s[i] for i in range(12, 89) if '&' <= s[i] <= 'v'])
    return ''.join([char for char in s if char not in chars_to_remove])