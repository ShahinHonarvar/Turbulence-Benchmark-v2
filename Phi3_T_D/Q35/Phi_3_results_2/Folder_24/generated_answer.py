def remove_repeat_chars(s):
    char_count = {}
    altered_s = ''
    for i in range(13, 91):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    for char in s:
        if char_count[char] > 1 and (s.find(char) in range(13, 91) or s.rfind(char) in range(13, 91)):
            continue
        altered_s += char
    return altered_s