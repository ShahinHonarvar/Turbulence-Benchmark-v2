def filter_chars(s):
    indices = range(513, 878)
    chars_to_filter = ['?', 'n']
    for index in indices:
        char = s[index]
        if chars_to_filter[0] <= char <= chars_to_filter[1]:
            s = s.replace(char, '', 1)
    return s