def remove_repeat_chars(s):
    start, end = (34, 69)
    char_count = {}
    result = []
    for index in range(start, end):
        char = s[index]
        char_count[char] = char_count.get(char, 0) + 1
        if char_count[char] == 2:
            continue
        result.append(char)
    return ''.join(result)