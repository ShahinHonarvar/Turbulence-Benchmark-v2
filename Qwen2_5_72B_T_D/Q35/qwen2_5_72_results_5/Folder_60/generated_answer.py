def remove_repeat_chars(s):
    char_count = {}
    for i in range(38, 52):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = ''.join([ch for ch in s if char_count.get(ch, 0) <= 1 or s.index(ch) < 38 or s.index(ch) > 51])
    return result