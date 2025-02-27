def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 72 < i < 93:
            if char in seen:
                continue
            if s.count(char, 72, 93) > 1:
                seen.add(char)
                continue
        result.append(char)
    return ''.join(result)