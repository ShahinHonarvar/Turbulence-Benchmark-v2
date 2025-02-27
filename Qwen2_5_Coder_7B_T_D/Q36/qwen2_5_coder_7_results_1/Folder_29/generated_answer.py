def filter_chars(s):
    chars_to_remove = set()
    for i in range(46, 68):
        char = chr(i)
        if 'H' < char < 's':
            chars_to_remove.add(char)
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result