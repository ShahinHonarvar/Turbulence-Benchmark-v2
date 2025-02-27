def filter_chars(s):
    index_range = range(46, 74)
    char_list = [char for i, char in enumerate(s) if i in index_range and '&' < char < 'M']
    for char in char_list:
        s = s.replace(char, '')
    return s