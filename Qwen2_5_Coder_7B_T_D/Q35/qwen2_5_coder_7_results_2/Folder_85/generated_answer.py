def remove_repeat_chars(s):
    char_count = {}
    for i in range(1, 8):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = []
    for char in s:
        if char_count[char] == 1 and char != s[0] and (char != s[-1]) or char_count[char] == 0:
            result.append(char)
    return ''.join(result)