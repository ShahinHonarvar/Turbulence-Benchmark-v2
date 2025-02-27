def remove_repeat_chars(s):
    char_count = {}
    for i in range(200, 203):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = [c for c in s if c not in char_count or char_count[c] == 1]
    return ''.join(result)