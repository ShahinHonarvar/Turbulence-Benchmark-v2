def remove_repeat_chars(s):
    char_count = {}
    for i in range(36, 85):
        if i < len(s):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = [char for char in s if char_count.get(char, 0) <= 1 or s.index(char) < 36 or s.index(char) >= 85]
    return ''.join(result)