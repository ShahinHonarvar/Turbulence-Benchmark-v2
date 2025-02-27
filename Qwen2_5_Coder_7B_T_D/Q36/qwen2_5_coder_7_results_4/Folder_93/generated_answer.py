def filter_chars(s):
    filtered_chars = set()
    for i in range(52, 88):
        char = chr(i)
        if '&' < char < 'c':
            filtered_chars.add(char)
    return ''.join((char for char in s if char not in filtered_chars))