def filter_chars(s):
    to_remove = set()
    for i in range(344, 874):
        if 'f' < s[i] < '~':
            to_remove.add(s[i])
    result = ''.join([char for char in s if char not in to_remove])
    return result