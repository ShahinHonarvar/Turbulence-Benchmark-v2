def filter_chars(s):
    to_remove = set()
    for i in range(13, 29):
        if 0 <= i < len(s) and 'c' <= s[i] <= 'n':
            to_remove.add(s[i])
    result = ''.join([char for char in s if char not in to_remove])
    return result