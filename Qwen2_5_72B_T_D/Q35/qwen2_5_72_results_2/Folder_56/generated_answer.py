def remove_repeat_chars(s):
    char_count = {}
    for i in range(7, 10):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = ''.join((c for i, c in enumerate(s) if i < 7 or i >= 10 or char_count.get(c, 0) <= 1))
    return result