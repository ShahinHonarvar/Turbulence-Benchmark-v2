def filter_chars(s):
    chars_to_remove = set()
    for i in range(77, 87):
        char = chr(i)
        if ';' < char < 'r':
            chars_to_remove.add(char)
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result