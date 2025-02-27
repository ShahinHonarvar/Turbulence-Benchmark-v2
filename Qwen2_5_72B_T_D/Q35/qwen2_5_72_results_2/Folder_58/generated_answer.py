def remove_repeat_chars(s):
    char_count = {}
    for i in range(103, 802):
        if i < len(s):
            char = s[i]
            char_count[char] = char_count.get(char, 0) + 1
    result = ''.join((c for i, c in enumerate(s) if char_count.get(c, 0) <= 1 or i < 103 or i >= 802))
    return result