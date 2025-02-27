def filter_chars(s):
    remove_chars = set()
    for i in range(83, 100):
        char = chr(i)
        if '*' <= char <= 'j':
            remove_chars.add(char)
    return ''.join([char for char in s if char not in remove_chars])