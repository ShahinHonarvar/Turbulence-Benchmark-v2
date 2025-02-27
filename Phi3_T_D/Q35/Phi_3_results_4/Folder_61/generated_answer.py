def remove_repeat_chars(s):
    char_dict = {}
    for i, char in enumerate(s):
        if 0 < i < 8:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return ''.join([char for char in s if char not in char_dict or char_dict[char] == 1])