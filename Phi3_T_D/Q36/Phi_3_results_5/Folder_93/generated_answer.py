def filter_chars(s):
    index_begin, index_end = (52, 88)
    for i in range(index_begin, index_end):
        char = s[i]
        if char > '&' and char < 'c':
            s = s.replace(char, '')
    return s