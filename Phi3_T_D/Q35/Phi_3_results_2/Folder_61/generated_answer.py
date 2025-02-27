def remove_repeat_chars(s):
    char_count = {}
    for i in range(8):
        char = s[i]
        if char in char_count:
            char_count[char] = False
        else:
            char_count[char] = True
    new_string = ''.join([char for i, char in enumerate(s) if (char_count[char] if i < 8 else True)])
    return new_string