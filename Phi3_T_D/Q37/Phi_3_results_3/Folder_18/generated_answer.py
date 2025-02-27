def filter_chars(s):
    modified_str = list(s)
    for i in range(770, 971):
        char = s[i]
        if '-' <= char <= 'D':
            modified_str.remove(char)
    return ''.join(modified_str)