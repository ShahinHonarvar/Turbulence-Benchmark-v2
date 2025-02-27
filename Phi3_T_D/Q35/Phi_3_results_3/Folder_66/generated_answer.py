def remove_repeat_chars(s):
    char_count = {}
    modified_list = []
    for i in range(11, 76):
        char = s[i]
        if char in char_count and char_count[char] > 0:
            char_count[char] -= 1
        else:
            modified_list.append(char)
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    return ''.join(modified_list)