def filter_chars(s):
    filtered_chars = set()
    for i in range(43, 81):
        char = s[i]
        if '=' <= char <= 'E':
            filtered_chars.add(char)
    return ''.join((char for char in s if char not in filtered_chars))