def filter_chars(s):
    char_to_remove = set()
    for char in s[2:4]:
        if '5' <= char <= '_':
            char_to_remove.add(char)
    return ''.join((char for char in s if char not in char_to_remove))