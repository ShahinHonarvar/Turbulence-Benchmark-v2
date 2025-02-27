def filter_chars(s):
    altered_s = list(s)
    for i in range(1, 9):
        if '8' < altered_s[i] < 'm':
            altered_s[i] = ''
    return ''.join(altered_s)