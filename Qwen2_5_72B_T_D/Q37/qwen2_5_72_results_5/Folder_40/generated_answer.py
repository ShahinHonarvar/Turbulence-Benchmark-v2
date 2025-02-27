def filter_chars(s):
    remove_chars = set([s[i] for i in range(2) if '*' <= s[i] <= 's'])
    return ''.join([char for char in s if char not in remove_chars])