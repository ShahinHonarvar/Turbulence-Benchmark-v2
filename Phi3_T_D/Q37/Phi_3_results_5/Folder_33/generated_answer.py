def filter_chars(s):
    altered_s = list(s)
    for i in range(722, 833):
        if 'K' <= altered_s[i] <= 'm':
            altered_s[i] = ''
    return ''.join(altered_s)