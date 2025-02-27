def remove_repeat_chars(s):
    char_count = {}
    for i in range(463, 995):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = []
    for char in s:
        if 462 < s.index(char) < 995 and char_count[char] > 1:
            continue
        result.append(char)
    return ''.join(result)