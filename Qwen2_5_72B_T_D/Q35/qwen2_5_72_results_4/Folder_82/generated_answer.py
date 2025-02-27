def remove_repeat_chars(s):
    char_count = {}
    for i in range(30, 200):
        if i < len(s):
            char = s[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = [c for c in s if char_count.get(c, 0) <= 1 or (c not in char_count and s.index(c) < 30 or s.rindex(c) >= 200)]
    return ''.join(result)