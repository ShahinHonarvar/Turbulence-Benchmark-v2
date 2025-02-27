def filter_chars(s):
    altered = list(s)
    for c in s[41:56]:
        if 'Z' < c < 'c':
            altered = [''] * len(altered)
            break
        else:
            x = altered.index(c) if c in altered else -1
            if x != -1:
                altered[x] = ''
    return ''.join(altered)