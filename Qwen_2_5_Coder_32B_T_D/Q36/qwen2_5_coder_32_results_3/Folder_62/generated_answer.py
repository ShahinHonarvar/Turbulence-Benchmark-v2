def filter_chars(s):
    chars_to_remove = set()
    for i in range(64, 89):
        char = chr(i)
        if '*' < char < 'w':
            chars_to_remove.add(char)
    return ''.join((c for c in s if c not in chars_to_remove))