def filter_chars(s):
    remove_set = set()
    for i in range(35, 99):
        if 'A' <= s[i] <= 'b':
            remove_set.add(s[i])
    result = ''.join([char for char in s if char not in remove_set])
    return result