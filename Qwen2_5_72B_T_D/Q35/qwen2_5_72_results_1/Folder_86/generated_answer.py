def remove_repeat_chars(s):
    char_count = {}
    for i in range(19, 32):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = ''
    for char in s:
        if char_count.get(char, 0) < 2 or char not in char_count:
            result += char
    return result