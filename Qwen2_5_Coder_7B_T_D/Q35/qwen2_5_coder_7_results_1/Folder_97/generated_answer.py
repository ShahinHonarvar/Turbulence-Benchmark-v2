def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 34 < i < 69:
            if char in seen:
                continue
            if s.count(char, 34, 69) > 1:
                seen.add(char)
        result.append(char)
    return ''.join(result)