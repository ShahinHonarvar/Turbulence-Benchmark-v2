def remove_repeat_chars(s):
    if len(s) <= 201:
        return s
    char_count = {}
    for i in range(51, 200):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    chars_to_remove = {k for k, v in char_count.items() if v > 1}
    return ''.join((c for c in s if c not in chars_to_remove))