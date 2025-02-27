def filter_chars(s):
    output = ''
    remove = set()
    for i, char in enumerate(s):
        if 69 < ord(char) < 106:
            remove.add(char)
    return ''.join((char for char in s if char not in remove))