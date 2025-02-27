def remove_repeat_chars(s):
    index = 0
    char_set = set()
    result = []
    while index < 2:
        if s[index] not in char_set:
            char_set.add(s[index])
        result.append(s[index])
        index += 1
    result.extend(s[2:])
    return ''.join(result)