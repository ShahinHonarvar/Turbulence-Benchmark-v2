def filter_chars(s):
    for i in range(43, 68):
        char_filter = chr(i)
        while char_filter in s:
            s = s.replace(char_filter, '')
    return s