def remove_repeat_chars(s):
    altered_string = []
    char_count = {}
    for i in range(len(s)):
        if 77 < i < 83:
            char = s[i]
            if char in char_count and char_count[char] == 0:
                char_count[char] -= 1
            else:
                char_count[char] = 1
        else:
            altered_string.append(s[i])
    for i in range(77, 83):
        char = s[i]
        if char_count.get(char, 0) > 0:
            char_count[char] -= 1
        else:
            altered_string.insert(i, char)
    return ''.join(altered_string)