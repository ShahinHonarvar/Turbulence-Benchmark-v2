def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if char in seen:
            continue
        if s.count(char, 0, 4) > 1:
            seen.add(char)
        else:
            result.append(char)
    return ''.join(result)