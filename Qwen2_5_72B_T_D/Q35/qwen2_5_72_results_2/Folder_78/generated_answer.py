def remove_repeat_chars(s):
    char_count = {}
    for i in range(63, 96):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars or not 63 <= s.index(char) <= 95))
    return result