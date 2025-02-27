def filter_chars(s):
    remove_set = set()
    for i in range(13, 29):
        if 0 <= i < len(s) and 'c' <= s[i] <= 'n':
            remove_set.add(s[i])
    return ''.join([char for char in s if char not in remove_set])