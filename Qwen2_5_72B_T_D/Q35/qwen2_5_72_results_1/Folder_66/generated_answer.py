def remove_repeat_chars(s):
    char_count = {}
    for i in range(11, 76):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = ''.join([ch for ch in s if char_count.get(ch, 0) <= 1 or s.index(ch) < 11 or s.index(ch) >= 76])
    return result