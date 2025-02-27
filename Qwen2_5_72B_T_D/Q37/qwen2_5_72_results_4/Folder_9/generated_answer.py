def filter_chars(s):
    to_remove = set()
    for i in range(38, 100):
        if 'A' <= s[i] <= 'Q':
            to_remove.add(s[i])
    result = ''.join([char for char in s if char not in to_remove])
    return result