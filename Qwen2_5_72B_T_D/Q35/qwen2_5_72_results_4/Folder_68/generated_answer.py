def remove_repeat_chars(s):
    char_count = {}
    for i in range(1, 9):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = ''.join([char for char in s if char_count.get(char, 0) < 2 or not 1 <= s.index(char) <= 8])
    return result