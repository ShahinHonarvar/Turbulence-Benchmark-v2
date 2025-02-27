def filter_chars(s):
    to_remove = set()
    for i in range(38, 100):
        char = s[i]
        if 'A' <= char <= 'Q':
            to_remove.add(char)
    result = ''.join([char for char in s if char not in to_remove])
    return result