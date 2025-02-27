def filter_chars(s):
    chars_to_remove = set()
    for i in range(46, 74):
        char = chr(i)
        if '&' < char < 'M':
            chars_to_remove.add(char)
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result