def remove_repeat_chars(s):
    char_count = {}
    for i in range(10 + 1, 79):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = ''.join([char for char in s if char not in chars_to_remove or s.index(char) < 10 or s.index(char) >= 79])
    return result