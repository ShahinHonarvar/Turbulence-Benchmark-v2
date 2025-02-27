def filter_chars(s):
    to_remove = set()
    for i in range(7, 9):
        char = s[i]
        if 'B' <= char <= 'H':
            to_remove.add(char)
    result = ''.join([char for char in s if char not in to_remove])
    return result