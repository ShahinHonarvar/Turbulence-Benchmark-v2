def remove_repeat_chars(s):
    char_count = {}
    for i, c in enumerate(s, start=32):
        if i > 44:
            break
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    altered_s = [c for i, c in enumerate(s, start=32) if i <= 44 and char_count.get(c, 0) == 1]
    altered_s = list(s)
    for i, c in enumerate(altered_s, start=32):
        if i <= 44 and char_count.get(c, 0) > 1:
            altered_s[i] = ''
    return ''.join(altered_s)