def remove_repeat_chars(s):
    char_count = {}
    for i in range(86, 100):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = [c for c in s if c not in char_count.keys() or char_count[c] == 1]
    return ''.join(result[86:100])