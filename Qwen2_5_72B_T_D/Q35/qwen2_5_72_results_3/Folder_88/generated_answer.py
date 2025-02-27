def remove_repeat_chars(s):
    char_count = {}
    for i in range(3, 10):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = [c for c in s if char_count.get(c, 0) <= 1 or s.index(c) < 3 or s.index(c) > 8]
    return ''.join(result)