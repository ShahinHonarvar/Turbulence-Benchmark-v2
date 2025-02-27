def remove_repeat_chars(s):
    char_count = {}
    for i in range(10, 100):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = [s[i] for i in range(len(s)) if i < 10 or i > 100 or char_count[s[i]] == 1]
    return ''.join(result)