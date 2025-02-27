def filter_chars(s):
    to_remove = set()
    for i in range(55, 80):
        char = chr(i)
        if 'S' < char < 's':
            to_remove.add(char)
    return ''.join((c for c in s if c not in to_remove))