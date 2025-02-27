def filter_chars(s):
    to_remove = set([s[i] for i in range(25, 98) if 'm' <= s[i] <= 'w'])
    return ''.join([char for char in s if char not in to_remove])