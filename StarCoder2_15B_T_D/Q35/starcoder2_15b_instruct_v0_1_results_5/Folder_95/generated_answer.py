def remove_repeat_chars(s):
    char_count = {}
    for char in s[32:99]:
        char_count[char] = char_count.get(char, 0) + 1
    for char, count in char_count.items():
        if count > 1:
            s = s.replace(char, '')
    return s