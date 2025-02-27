def remove_repeat_chars(s):
    char_count = {}
    for i in range(103, 802):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = [s[i] for i in range(len(s)) if i < 103 or i >= 802 or char_count[s[i]] == 1]
    return ''.join(result)