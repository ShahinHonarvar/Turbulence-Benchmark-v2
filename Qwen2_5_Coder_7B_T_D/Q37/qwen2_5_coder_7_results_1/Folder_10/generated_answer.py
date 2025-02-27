def filter_chars(s):
    to_remove = set()
    for i in range(63, 85):
        char = chr(i)
        if 'E' <= char <= '~':
            to_remove.add(char)
    return ''.join([char for char in s if char not in to_remove])