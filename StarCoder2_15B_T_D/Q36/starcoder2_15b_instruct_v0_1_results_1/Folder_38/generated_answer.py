def filter_chars(s):
    s_list = list(s)
    for i in range(44, 48):
        if '+' < s_list[i] < 'l':
            s_list = [c for c in s_list if c != s_list[i]]
    return ''.join(s_list)