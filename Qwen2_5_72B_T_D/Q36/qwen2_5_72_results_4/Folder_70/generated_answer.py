def filter_chars(s):
    to_remove = set([s[i] for i in range(170, 195) if '!' < s[i] < '}'])
    return ''.join([char for char in s if char not in to_remove])