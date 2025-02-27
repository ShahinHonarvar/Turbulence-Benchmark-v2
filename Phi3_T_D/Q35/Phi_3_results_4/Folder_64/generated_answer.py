def remove_repeat_chars(s):
    char_count = {}
    result = ''
    for i in range(6):
        char = s[i]
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
        if char_count[char] == 1:
            result += char
    return result + s[6:]