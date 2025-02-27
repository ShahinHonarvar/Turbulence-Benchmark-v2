def remove_repeat_chars(s):
    char_count = {}
    for i in range(11, 76):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = [c for c in s if char_count.get(c, 0) < 2 or not 11 <= s.index(c) < 76]
    return ''.join(result)