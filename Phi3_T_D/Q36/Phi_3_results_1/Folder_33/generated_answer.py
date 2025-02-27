def filter_chars(s):
    chars_to_remove = set()
    for i in range(300, 419):
        char = s[i]
        if '9' < char < 'P':
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))