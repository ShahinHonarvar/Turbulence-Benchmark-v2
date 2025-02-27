def filter_chars(s):
    char_to_filter = ''
    for idx in range(3, 5):
        if 'Y' < s[idx] < 's':
            char_to_filter += s[idx]
    return s.replace(char_to_filter, '')