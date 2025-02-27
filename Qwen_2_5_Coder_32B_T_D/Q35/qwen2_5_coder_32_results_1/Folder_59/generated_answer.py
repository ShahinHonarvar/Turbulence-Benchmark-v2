def remove_repeat_chars(s):
    substring = s[1:10]
    char_count = {}
    for char in substring:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = []
    for char in s:
        if char not in char_count or char_count[char] == 1:
            result.append(char)
    return ''.join(result)