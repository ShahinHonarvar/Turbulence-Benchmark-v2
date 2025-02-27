def remove_repeat_chars(s):
    char_count = {}
    for i in range(35, 64):
        if i < len(s):
            char = s[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = ''.join((c for i, c in enumerate(s) if c not in char_count or char_count[c] == 1 or i < 35 or (i >= 64)))
    return result