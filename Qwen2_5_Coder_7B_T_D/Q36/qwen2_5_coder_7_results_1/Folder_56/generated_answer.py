def filter_chars(s):
    chars_to_remove = set()
    for i in range(31, 50):
        char = chr(i)
        if '/' < char < 'J':
            chars_to_remove.add(char)
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result