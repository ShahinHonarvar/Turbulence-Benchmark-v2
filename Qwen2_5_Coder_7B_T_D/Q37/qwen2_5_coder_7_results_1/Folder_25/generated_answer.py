def filter_chars(s):
    chars_to_remove = set()
    for i in range(31, 39):
        char = s[i]
        if ';' <= char <= 'g':
            chars_to_remove.add(char)
    return ''.join([char for char in s if char not in chars_to_remove])