def remove_repeat_chars(s):
    char_count = {}
    for i in range(13, 91):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = [s[i] for i in range(len(s)) if i < 13 or i > 90 or char_count[s[i]] == 1]
    return ''.join(result)