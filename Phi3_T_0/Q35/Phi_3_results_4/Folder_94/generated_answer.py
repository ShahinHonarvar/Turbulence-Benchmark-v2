def remove_repeat_chars(s):
    start, end = (42, 88)
    seen = set()
    result = []
    for i in range(start, end):
        char = s[i]
        if char in seen:
            continue
        if s.count(char, start, end) > 1:
            seen.add(char)
        else:
            result.append(char)
    return ''.join(result)