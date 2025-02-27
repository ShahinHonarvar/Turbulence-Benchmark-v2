def remove_repeat_chars(s):
    check_range = s[22:25]
    for char in set(check_range):
        if check_range.count(char) > 1:
            s = s.replace(char, '')
    return s