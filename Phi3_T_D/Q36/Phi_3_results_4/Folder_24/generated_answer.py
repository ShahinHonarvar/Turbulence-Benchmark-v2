def filter_chars(s):
    altered_s = ''
    for i in range(10, 16):
        if 't' < s[i] < 'v':
            altered_s = altered_s + s[i]
        else:
            altered_s = altered_s + s[i]
    return altered_s