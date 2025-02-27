def remove_repeat_chars(s):
    start, end = (56, 90)
    char_count = {}
    result = []
    for i, char in enumerate(s):
        if start <= i < end:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    for i, char in enumerate(s):
        if start <= i < end:
            if char_count[char] > 1:
                char_count[char] = 0
            else:
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)