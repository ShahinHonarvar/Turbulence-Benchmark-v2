def remove_repeat_chars(s):
    char_count = {}
    for i in range(25, 80):
        if i < len(s):
            char = s[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = ''.join([c for c in s if char_count.get(c, 0) <= 1 or (s.index(c) < 25 or s.index(c) >= 80)])
    return result