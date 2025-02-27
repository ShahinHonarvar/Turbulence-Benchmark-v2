def remove_repeat_chars(s):
    char_count = {}
    for i in range(68, 100):
        if i < len(s):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = ''.join((char for char in s if char_count.get(char, 1) == 1 or not 68 <= s.index(char) < 100))
    return result