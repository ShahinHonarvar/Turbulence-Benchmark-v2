def remove_repeat_chars(s):
    char_count = {}
    for i in range(1, 7):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = [char for char in s if char not in char_count or char_count[char] < 2]
    return ''.join(result)