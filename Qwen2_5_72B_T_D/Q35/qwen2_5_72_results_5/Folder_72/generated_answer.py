def remove_repeat_chars(s):
    char_count = {}
    for i in range(13, 70):
        if i < len(s):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = ''
    for i in range(len(s)):
        if i < 13 or i >= 70 or char_count.get(s[i], 0) == 1:
            result += s[i]
    return result