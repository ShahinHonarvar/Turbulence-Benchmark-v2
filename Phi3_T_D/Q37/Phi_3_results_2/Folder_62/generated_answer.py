def filter_chars(s):
    s_list = list(s[10:70])
    for i, char in enumerate(s_list):
        if 'I' <= char <= 'K':
            s_list[i] = ''
    return ''.join(s_list) + s[70:]