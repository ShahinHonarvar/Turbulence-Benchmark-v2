def filter_chars(s):
    to_remove = set()
    for i in range(27, 75):
        if 'A' < chr(i) < 'i':
            to_remove.add(chr(i))
    return ''.join((c for c in s if c not in to_remove))