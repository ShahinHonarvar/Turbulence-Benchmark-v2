def filter_chars(s):
    altered_str = ''
    for i in range(46, 68):
        if 'H' < s[i] < 's':
            altered_str += s[i]
        else:
            altered_str += s[45]
    return altered_str