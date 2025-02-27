def remove_repeat_chars(s):
    char_count = {}
    for i in range(17, 87):
        if i < len(s):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = ''.join([char for char in s if char_count.get(char, 0) <= 1 or s.index(char) < 17 or s.index(char) >= 87])
    return result