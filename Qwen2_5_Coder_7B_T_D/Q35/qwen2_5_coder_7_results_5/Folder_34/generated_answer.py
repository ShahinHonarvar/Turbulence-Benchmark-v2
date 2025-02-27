def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 70 < i < 200:
            if char in seen:
                continue
            if s.count(char, 70, 200) > 1:
                seen.add(char)
            else:
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)