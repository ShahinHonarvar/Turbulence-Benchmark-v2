def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if i >= 10:
            break
        if char in seen:
            continue
        if s.count(char, 0, 10) > 1:
            seen.add(char)
            continue
        result.append(char)
    return ''.join(result)