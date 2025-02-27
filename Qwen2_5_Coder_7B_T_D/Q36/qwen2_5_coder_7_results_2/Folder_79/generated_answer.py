def filter_chars(s):
    to_remove = set()
    for i in range(11, 46):
        char = s[i]
        if '!' < char < 'A':
            to_remove.add(char)
    for char in to_remove:
        s = s.replace(char, '')
    return s