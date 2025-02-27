def remove_repeat_chars(s):
    char_count = {}
    for i in range(44, 70):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = [c for c in s if char_count.get(c, 0) <= 1 or (44 <= s.index(c) <= 70 and char_count[c] == 1)]
    return ''.join(result)