def remove_repeat_chars(s):
    char_count = {}
    for i in range(29, 53):
        if i < len(s):
            char = s[i]
            char_count[char] = char_count.get(char, 0) + 1
    result = ''.join([char for char in s if char_count.get(char, 1) < 2 or (s.index(char) < 29 or s.index(char) >= 53)])
    return result