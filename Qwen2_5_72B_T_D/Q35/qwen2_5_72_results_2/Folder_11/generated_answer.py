def remove_repeat_chars(s):
    char_count = {}
    for i in range(1, len(s)):
        if 48 < i < 76:
            if s[i] in char_count:
                char_count[s[i]] += 1
            else:
                char_count[s[i]] = 1
    result = ''
    for i in range(len(s)):
        if s[i] not in char_count or char_count[s[i]] == 1:
            result += s[i]
    return result