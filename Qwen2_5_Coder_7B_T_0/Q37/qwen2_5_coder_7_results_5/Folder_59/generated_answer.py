def filter_chars(s):
    chars_to_remove = set()
    for i in range(2, 4):
        char = s[i]
        if '5' <= char <= '_':
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))