def remove_repeat_chars(s):
    char_count = {}
    for i in range(11):
        char = s[i]
        if i > 0:
            char_count[char] = char_count.get(char, 0) + 1
    return ''.join((c for i, c in enumerate(s) if i > 0 and c not in char_count or char_count[c] == 1))