def filter_chars(s):
    chars_to_remove = set()
    for i in range(50, 92):
        char = chr(i)
        if 'A' < char < 'Q':
            chars_to_remove.add(char)
    result = ''.join([c for c in s if c not in chars_to_remove])
    return result