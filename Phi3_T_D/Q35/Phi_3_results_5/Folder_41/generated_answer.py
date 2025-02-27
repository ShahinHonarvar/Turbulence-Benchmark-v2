def remove_repeat_chars(s):
    target_chars = {}
    for i in range(3, 8):
        if s[i] in target_chars:
            target_chars[s[i]] += 1
        else:
            target_chars[s[i]] = 1
    return ''.join([c for i, c in enumerate(s) if i < 3 or i > 7 or target_chars[c] == 1])