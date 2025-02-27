def remove_repeat_chars(s):
    char_count = {}
    for i in range(16, 87):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = ''.join([char for char in s if char_count.get(char, 0) <= 1 or (0 <= s.index(char) <= 16 or 87 <= s.index(char) <= len(s))])
    return result