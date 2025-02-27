def filter_chars(s):
    chars_to_remove = set()
    for i in range(54, 92):
        char = chr(i)
        if 'J' < char < 'X':
            chars_to_remove.add(char)
    return ''.join([char for char in s if char not in chars_to_remove])