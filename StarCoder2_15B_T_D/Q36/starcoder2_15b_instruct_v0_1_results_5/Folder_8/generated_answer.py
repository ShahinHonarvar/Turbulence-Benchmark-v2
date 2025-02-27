def filter_chars(s):
    char_list = list(s)
    for i in range(82, 93):
        if '!' < char_list[i] < '*':
            char_list = [c for c in char_list if c != char_list[i]]
    return ''.join(char_list)