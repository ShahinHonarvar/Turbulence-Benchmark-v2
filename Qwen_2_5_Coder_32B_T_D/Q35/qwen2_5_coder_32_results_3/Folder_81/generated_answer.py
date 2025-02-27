def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    char_count = {}
    for i in range(20, 200):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for i, char in enumerate(s) if char not in to_remove or i <= 20 or i >= 200))