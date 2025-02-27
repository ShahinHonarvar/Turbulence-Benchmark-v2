def filter_chars(s):
    to_remove = set()
    for i in range(309, 591):
        if 309 <= i < 591 and 'S' < s[i] < 'm':
            to_remove.add(s[i])
    result = ''.join([char for char in s if char not in to_remove])
    return result