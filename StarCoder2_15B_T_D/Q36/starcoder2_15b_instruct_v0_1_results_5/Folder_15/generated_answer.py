def filter_chars(s):
    if len(s) < 7:
        return s
    s_list = list(s)
    for i in range(2, 7):
        if s_list[i] > 'h' and s_list[i] < 'k':
            s_list = [c for c in s_list if c != s_list[i]]
    return ''.join(s_list)