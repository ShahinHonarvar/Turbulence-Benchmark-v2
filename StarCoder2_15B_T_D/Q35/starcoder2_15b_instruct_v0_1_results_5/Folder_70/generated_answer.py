def remove_repeat_chars(s):
    char_count = {}
    for c in s[43:70]:
        char_count[c] = char_count.get(c, 0) + 1
    for c in set(s[43:70]):
        if char_count[c] > 1:
            s = s.replace(c, '')
    return s