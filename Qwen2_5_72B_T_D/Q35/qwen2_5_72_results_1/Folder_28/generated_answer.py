def remove_repeat_chars(s):
    char_count = {}
    for i in range(86, 99):
        if i < len(s):
            char = s[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = ''.join([c for c in s if char_count.get(c, 0) <= 1 or not 86 <= s.index(c) < 99])
    return result