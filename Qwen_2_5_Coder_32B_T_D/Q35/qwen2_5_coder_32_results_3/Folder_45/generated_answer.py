def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    char_count = {}
    for i in range(41, 200):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in repeat_chars))