def filter_chars(s):
    to_remove = set()
    for i in range(10, 15):
        if 't' < s[i] < 'v':
            to_remove.add(s[i])
    return ''.join([char for char in s if char not in to_remove])