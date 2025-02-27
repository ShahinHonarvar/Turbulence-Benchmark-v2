def filter_chars(s):
    to_remove = set()
    for i in range(46, 68):
        char = chr(i)
        if 'H' < char < 's':
            to_remove.add(char)
    for char in to_remove:
        s = s.replace(char, '')
    return s