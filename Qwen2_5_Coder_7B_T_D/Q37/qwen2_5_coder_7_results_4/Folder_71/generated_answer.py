def filter_chars(s):
    to_remove = set()
    for i in range(32, 47):
        for char in s:
            if char >= '0' and char <= 'k' and (ord(char) == i):
                to_remove.add(char)
    return ''.join([char for char in s if char not in to_remove])