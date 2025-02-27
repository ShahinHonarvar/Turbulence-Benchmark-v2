def filter_chars(s):
    to_remove = set()
    for i in range(13, 29):
        char = s[i]
        if 'c' <= char <= 'n':
            to_remove.add(char)
    result = ''.join([char for char in s if char not in to_remove])
    return result