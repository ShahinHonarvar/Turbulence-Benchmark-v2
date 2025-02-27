def filter_chars(s):
    altered_string = list(s)
    for i in range(20, 80):
        if '!' <= altered_string[i] <= 'T':
            altered_string[i] = ''
    return ''.join(altered_string)