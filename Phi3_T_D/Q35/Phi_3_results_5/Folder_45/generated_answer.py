def remove_repeat_chars(s):
    char_count = {}
    unique_chars = []
    for i, char in enumerate(s):
        if 40 < i < 200 and char in char_count:
            continue
        if char not in char_count:
            char_count[char] = 1
            unique_chars.append(char)
        else:
            del char_count[char]
    return ''.join(unique_chars)