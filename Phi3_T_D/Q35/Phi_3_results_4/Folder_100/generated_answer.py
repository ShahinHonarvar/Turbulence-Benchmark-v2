def remove_repeat_chars(s):
    char_count = {}
    for i in range(44, 78):
        char = s[i]
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    new_s = []
    for char in s:
        if char_count.get(char, 0) <= 1 or not 44 <= s.index(char) < 78:
            new_s.append(char)
    return ''.join(new_s)