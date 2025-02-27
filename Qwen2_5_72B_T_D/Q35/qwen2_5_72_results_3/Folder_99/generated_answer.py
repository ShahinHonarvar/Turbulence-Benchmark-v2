def remove_repeat_chars(s):
    char_count = {}
    for i in range(450, 905):
        if i < len(s):
            char = s[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = ''.join((c for i, c in enumerate(s) if i < 450 or i >= 905 or char_count.get(c, 0) == 1))
    return result