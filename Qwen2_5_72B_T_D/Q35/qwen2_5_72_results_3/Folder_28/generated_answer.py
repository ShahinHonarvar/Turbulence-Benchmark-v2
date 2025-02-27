def remove_repeat_chars(s):
    char_count = {}
    for i in range(86, 99):
        if i < len(s):
            char = s[i]
            char_count[char] = char_count.get(char, 0) + 1
    result = ''.join([c for c in s if char_count.get(c, 0) <= 1])
    return result