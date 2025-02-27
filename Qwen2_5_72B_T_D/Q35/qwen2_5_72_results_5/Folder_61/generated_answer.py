def remove_repeat_chars(s):
    char_count = {}
    for i in range(1, 8):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = ''.join([char for char in s if char_count.get(char, 0) < 2 or s.index(char) not in range(1, 8)])
    return result