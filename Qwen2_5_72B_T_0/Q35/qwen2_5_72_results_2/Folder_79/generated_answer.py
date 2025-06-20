def remove_repeat_chars(s):
    char_count = {}
    for i in range(1, 7):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = ''.join([char for char in s if char not in char_count or char_count[char] == 1])
    return result