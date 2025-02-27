def filter_chars(s):
    char_to_remove = [chr(i) for i in range(34, 65) if chr(i) > '>' and chr(i) < 'A']
    for char in char_to_remove:
        s = s.replace(char, '')
    return s