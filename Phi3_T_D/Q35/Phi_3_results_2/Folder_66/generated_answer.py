def remove_repeat_chars(s):
    start, end = (11, 76)
    seen = set()
    s_list = list(s)
    result = []
    for i in range(start, end):
        char = s_list[i]
        if char in seen:
            continue
        else:
            seen.add(char)
            result.append(char)
    return ''.join(result)