def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 30 < i < 200:
            if s.count(char, 30, 200) > 1 and char not in seen:
                seen.add(char)
            elif char not in seen:
                result.append(char)
    return ''.join(result)