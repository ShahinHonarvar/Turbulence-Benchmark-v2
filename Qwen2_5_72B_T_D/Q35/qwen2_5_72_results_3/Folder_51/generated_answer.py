def remove_repeat_chars(s):
    char_count = {}
    for i in range(6, 10):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = ''
    for i in range(len(s)):
        if i < 6 or i >= 10 or char_count.get(s[i], 0) < 2:
            result += s[i]
    return result