def filter_chars(s):
    char_range = 'b'
    for i in range(477, 948):
        if char_range < s[i] < 'd':
            s = s.replace(s[i], '', s.count(s[i]))
    return s