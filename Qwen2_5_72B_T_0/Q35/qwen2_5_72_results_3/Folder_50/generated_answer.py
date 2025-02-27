def remove_repeat_chars(s):
    char_count = {}
    for i in range(13, 76):
        if i < len(s):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = ''.join((c for i, c in enumerate(s) if i < 13 or i >= 76 or char_count.get(c, 0) == 1))
    return result