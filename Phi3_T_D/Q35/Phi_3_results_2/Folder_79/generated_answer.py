def remove_repeat_chars(s):
    char_count = {}
    for i, char in enumerate(s[1:7]):
        char_count[char] = char_count.get(char, 0) + 1
    return ''.join([char for char in s if char not in char_count or char_count[char] <= 1])