def remove_repeat_chars(s):
    start, end = (100, 200)
    char_set = set()
    i = start
    while i < end:
        if s[i] in char_set:
            s = s[:i] + s[i + 1:]
            i -= 1
        else:
            char_set.add(s[i])
            i += 1
    return s