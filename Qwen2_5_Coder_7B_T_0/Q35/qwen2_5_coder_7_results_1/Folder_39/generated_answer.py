def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 44 < i < 91:
            if char in seen:
                continue
            if s.count(char, 44, 91) > 1:
                seen.add(char)
        result.append(char)
    return ''.join(result)