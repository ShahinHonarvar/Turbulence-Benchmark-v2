def remove_repeat_chars(s):
    char_count = {}
    for i in range(125, 825):
        if i < len(s):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = ''.join((c for i, c in enumerate(s) if c not in char_count or char_count[c] == 1 or i <= 125 or (i >= 825)))
    return result