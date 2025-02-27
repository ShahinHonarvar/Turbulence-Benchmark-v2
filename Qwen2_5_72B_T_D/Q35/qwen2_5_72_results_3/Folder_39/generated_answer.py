def remove_repeat_chars(s):
    char_count = {}
    for i in range(45, 91):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = ''
    for char in s:
        if 45 <= s.index(char) <= 90 and char_count.get(char, 0) > 1:
            continue
        result += char
    return result