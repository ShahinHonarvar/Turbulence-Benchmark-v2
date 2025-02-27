def filter_chars(s):
    to_remove = set()
    for i in range(29, 80):
        char = s[i]
        if 'K' <= char <= 'z':
            to_remove.add(char)
    result = ''.join([char for char in s if char not in to_remove])
    return result