def remove_repeat_chars(s):
    char_count = {}
    for i in range(355, 988):
        if i < len(s):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = ''.join((c for i, c in enumerate(s) if i < 355 or i >= 988 or char_count.get(c, 0) == 1))
    return result