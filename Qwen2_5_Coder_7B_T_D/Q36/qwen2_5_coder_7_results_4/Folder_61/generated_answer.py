def filter_chars(s):
    to_remove = set()
    for i in range(3, 9):
        char = s[i]
        if '*' < char < 'E':
            to_remove.add(char)
    return ''.join((c for c in s if c not in to_remove))