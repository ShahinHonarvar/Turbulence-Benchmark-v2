def filter_chars(s):
    to_remove = set()
    for i in range(52, 82):
        if 'A' <= s[i] <= 'U':
            to_remove.add(s[i])
    return ''.join([char for char in s if char not in to_remove])