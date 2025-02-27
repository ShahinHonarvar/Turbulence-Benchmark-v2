def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 10 < i < 100:
            if s.count(char, 10, 100) > 1 and char not in seen:
                seen.add(char)
            elif char not in seen:
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)