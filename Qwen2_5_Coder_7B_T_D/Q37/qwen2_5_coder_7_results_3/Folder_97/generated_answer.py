def filter_chars(s):
    to_remove = set()
    for i in range(227, 236):
        char = s[i]
        if 'D' <= char <= 'u':
            to_remove.add(char)
    result = ''.join((char for char in s if char not in to_remove))
    return result