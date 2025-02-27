def remove_repeat_chars(s):
    char_count = {}
    for i in range(32, 44):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = [char for char in s if char_count.get(char, 0) <= 1 or (32 <= s.index(char) <= 44 and char_count[char] == 1)]
    return ''.join(result)