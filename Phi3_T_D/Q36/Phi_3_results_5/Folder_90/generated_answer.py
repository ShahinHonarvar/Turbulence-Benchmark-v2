def filter_chars(s):
    filtered_string = ''
    for i in range(344, 874):
        if 'f' < s[i] < '~':
            continue
        else:
            filtered_string += s[i]
    return filtered_string