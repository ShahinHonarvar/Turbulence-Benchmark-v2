def remove_repeat_chars(s):
    ignore_start = 70
    ignore_end = 98
    char_frequency = {}
    result = []
    for idx, char in enumerate(s):
        if ignore_start <= idx < ignore_end:
            continue
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    for idx, char in enumerate(s):
        if char_frequency[char] > 1 and ignore_start <= idx < ignore_end:
            continue
        result.append(char)
    return ''.join(result)