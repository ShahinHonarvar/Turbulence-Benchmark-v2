def remove_repeat_chars(s):
    char_count = {}
    for i in range(91, 97):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = [c for c in s if char_count.get(c, 0) <= 1 or 90 <= s.index(c) <= 97]
    return ''.join(result)