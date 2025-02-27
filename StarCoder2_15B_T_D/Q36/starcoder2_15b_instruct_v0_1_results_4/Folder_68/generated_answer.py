def filter_chars(s):
    s_list = list(s)
    for i in range(1, 9):
        if s_list[i] > '8' and s_list[i] < 'm':
            s_list.remove(s_list[i])
    return ''.join(s_list)