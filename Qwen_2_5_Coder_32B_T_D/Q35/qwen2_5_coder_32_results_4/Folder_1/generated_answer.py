def remove_repeat_chars(s):
    if len(s) <= 88:
        return s
    segment = s[17:88]
    char_count = {}
    for char in segment:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    to_remove = set((char for char, count in char_count.items() if count > 1))
    result = ''.join((char for char in s if char not in to_remove))
    return result