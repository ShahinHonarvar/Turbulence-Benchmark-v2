def remove_repeat_chars(s):
    char_count = {}
    for i in range(2, 6):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = ''.join((c for c in s if char_count.get(c, 0) < 2 or not 2 <= i < 6))
    return result