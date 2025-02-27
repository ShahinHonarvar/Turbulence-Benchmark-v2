def remove_repeat_chars(s):
    indices = range(91, 98)
    char_set = set()
    result = []
    for i, char in enumerate(s):
        if i in indices and char not in char_set:
            char_set.add(char)
        elif i in indices and char in char_set:
            continue
        else:
            result.append(char)
    return ''.join(result)