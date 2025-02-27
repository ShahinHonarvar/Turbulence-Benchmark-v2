def filter_chars(s):
    for i in range(770, 971):
        if ',-D'[0] <= s[i] <= ',-D'[3]:
            s = s.replace(s[i], '')
    return s