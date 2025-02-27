def remove_repeat_chars(s):
    char_count = {}
    for i in range(20, 51):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = [s[i] for i in range(len(s)) if i < 20 or i > 50 or char_count[s[i]] == 1]
    return ''.join(result)