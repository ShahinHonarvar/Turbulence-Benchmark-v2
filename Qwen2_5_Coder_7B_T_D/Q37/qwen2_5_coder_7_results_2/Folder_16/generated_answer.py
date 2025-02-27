def filter_chars(s):
    chars_to_remove = set()
    for i in range(225, 382):
        char = s[i]
        if 'D' <= char <= 'Y':
            chars_to_remove.add(char)
    return ''.join([char for char in s if char not in chars_to_remove])