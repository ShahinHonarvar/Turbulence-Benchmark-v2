def remove_repeat_chars(s):
    sub_str = s[17:88]
    char_count = {}
    for char in sub_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = []
    for char in s:
        if char_count.get(char, 0) > 1 and 17 <= s.index(char) < 88:
            result.append(char)
        elif char_count.get(char, 0) == 1 or 88 <= s.index(char) < 17 or s.index(char) >= len(s) - (88 - len(sub_str)):
            result.append(char)
    return ''.join(result)