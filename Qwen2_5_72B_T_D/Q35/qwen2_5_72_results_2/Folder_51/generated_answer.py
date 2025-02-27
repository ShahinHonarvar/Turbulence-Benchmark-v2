def remove_repeat_chars(s):
    char_count = {}
    for i in range(6, 10):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = ''.join((c for i, c in enumerate(s) if i < 6 or i >= 10 or char_count.get(c, 0) == 1))
    return result