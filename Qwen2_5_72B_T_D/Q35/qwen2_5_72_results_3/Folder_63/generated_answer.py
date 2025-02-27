def remove_repeat_chars(s):
    char_count = {}
    for i in range(81, 86):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = ''.join((c for c in s if char_count.get(c, 0) <= 1 or s.index(c) < 81 or s.index(c) > 85))
    return result