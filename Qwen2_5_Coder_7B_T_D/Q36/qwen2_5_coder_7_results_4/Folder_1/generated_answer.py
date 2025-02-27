def filter_chars(s):
    chars_to_remove = set()
    for i in range(69, 87):
        if '#' < chr(i) < 'L':
            chars_to_remove.add(chr(i))
    return ''.join((c for c in s if c not in chars_to_remove))