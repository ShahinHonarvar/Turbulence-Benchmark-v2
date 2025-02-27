def filter_chars(s):
    to_remove = set()
    for i in range(25, 98):
        char = s[i] if i < len(s) else ''
        if 'm' <= char <= 'w':
            to_remove.add(char)
    result = ''.join([char for char in s if char not in to_remove])
    return result