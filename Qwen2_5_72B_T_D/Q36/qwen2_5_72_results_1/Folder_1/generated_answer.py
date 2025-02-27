def filter_chars(s):
    remove_set = set()
    for i in range(69, 87):
        if s[i] > '#' and s[i] < 'L':
            remove_set.add(s[i])
    result = ''.join([char for char in s if char not in remove_set])
    return result