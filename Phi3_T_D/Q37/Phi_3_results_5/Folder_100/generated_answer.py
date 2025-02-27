def filter_chars(s):
    chars_to_remove = set()
    for i in range(88, 91):
        char = s[i]
        if 'J' <= char <= 'Q':
            chars_to_remove.add(char)
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result