def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if char in seen:
            continue
        if s.count(char, 1, 10) > 0:
            seen.add(char)
        else:
            result.append(char)
    return ''.join(result)