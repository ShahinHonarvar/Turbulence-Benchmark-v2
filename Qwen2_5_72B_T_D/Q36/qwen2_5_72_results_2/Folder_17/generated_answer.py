def filter_chars(s):
    to_remove = set()
    for i in range(18, 95):
        if 'K' < s[i] < 'a':
            to_remove.add(s[i])
    result = ''.join([char for char in s if char not in to_remove])
    return result