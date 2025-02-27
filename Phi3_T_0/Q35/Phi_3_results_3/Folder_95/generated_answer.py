def remove_repeat_chars(s):
    char_count = {}
    for i, char in enumerate(s[32:98]):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return ''.join([char for i, char in enumerate(s) if (char not in char_count or char_count[char] == 1) or i < 32 or i >= 98])