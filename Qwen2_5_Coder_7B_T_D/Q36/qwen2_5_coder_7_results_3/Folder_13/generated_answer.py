def filter_chars(s):
    to_remove = set()
    for i in range(324, 526):
        char = chr(i)
        if ')' < char < 'O':
            to_remove.add(char)
    return ''.join((char for char in s if char not in to_remove))