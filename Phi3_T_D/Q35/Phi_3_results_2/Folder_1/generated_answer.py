def remove_repeat_chars(s):
    start, end = (17, 88)
    seen_chars = set()
    result = []
    for i in range(start, end):
        char = s[i]
        if char in seen_chars:
            continue
        if s.count(char, start, end) > 1:
            result.append(char)
            seen_chars.add(char)
    return ''.join(result)