def remove_repeat_chars(s):
    if len(s) <= 81:
        return s
    substring = s[26:80]
    char_count = {}
    for char in substring:
        char_count[char] = char_count.get(char, 0) + 1
    repeat_chars = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in repeat_chars))