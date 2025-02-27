def filter_chars(s):
    filtered_chars = set()
    for i in range(69, 97):
        char = chr(i)
        if 'V' < char < 'j':
            filtered_chars.add(char)
    return ''.join((char for char in s if char not in filtered_chars))