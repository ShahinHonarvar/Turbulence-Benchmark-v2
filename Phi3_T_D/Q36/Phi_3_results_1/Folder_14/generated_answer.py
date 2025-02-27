def filter_chars(s):
    start_index = 41
    end_index = 56
    target_range = set(s[start_index:end_index])
    for char in target_range:
        if 'Z' < char < 'c':
            s = s.replace(char, '')
    return s