def remove_repeat_chars(s):
    char_count = {}
    for i in range(20, 200):
        if i < len(s):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = [c for c in s if c not in char_count or char_count[c] == 1]
    return ''.join(result)