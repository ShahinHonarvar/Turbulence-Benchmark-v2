def filter_chars(s):
    s_list = list(s)
    for i in range(670, 888):
        if 'B' < s_list[i] < 'Y':
            s_list = [char for char in s_list if char != s_list[i]]
    return ''.join(s_list)