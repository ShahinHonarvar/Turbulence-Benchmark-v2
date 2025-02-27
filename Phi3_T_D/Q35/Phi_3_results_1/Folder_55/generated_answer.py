def remove_repeat_chars(s):
    indices = set(range(10, 100))
    char_count = {}
    new_string = []
    for index, char in enumerate(s):
        if index not in indices:
            new_string.append(char)
            continue
        if char in char_count and char_count[char] < 2:
            char_count[char] += 1
            new_string.append(char)
        elif char not in char_count:
            char_count[char] = 1
            new_string.append(char)
        else:
            char_count[char] = 1
            continue
    return ''.join(new_string)