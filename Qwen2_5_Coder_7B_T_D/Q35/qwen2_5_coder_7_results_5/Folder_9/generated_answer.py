def remove_repeat_chars(s):
    char_count = {}
    for i in range(80, 200):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = ''
    for char in s:
        if char_count[char] == 1 or (char_count[char] > 1 and s.index(char) < 80 or s.index(char) >= 200):
            result += char
    return result