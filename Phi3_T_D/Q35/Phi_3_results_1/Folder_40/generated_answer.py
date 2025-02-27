def remove_repeat_chars(s):
    char_count = {char: 0 for char in set(s[0:4])}
    for char in s[0:4]:
        char_count[char] += 1
    return ''.join([char for char in s if char not in char_count or char_count[char] == 1])