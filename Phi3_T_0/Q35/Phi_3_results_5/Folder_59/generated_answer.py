def remove_repeat_chars(s):
    char_count = {}
    for i in range(11):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = [c for c in s if char_count[c] == 1 or i < 0 or i > 10]
    return ''.join(result)