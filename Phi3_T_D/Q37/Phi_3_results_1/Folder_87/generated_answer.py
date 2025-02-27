def filter_chars(s):
    for i in range(18, 82):
        chr_val = ord(s[i])
        if 'W' <= s[i] <= '[':
            s = s.replace(s[i], '')
    return s