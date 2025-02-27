def remove_repeat_chars(s):
    char_count = {}
    for i in range(50, 74):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = [c for c in s if char_count.get(c, 0) <= 1 or s.index(c) < 50 or s.index(c) >= 74]
    return ''.join(result)