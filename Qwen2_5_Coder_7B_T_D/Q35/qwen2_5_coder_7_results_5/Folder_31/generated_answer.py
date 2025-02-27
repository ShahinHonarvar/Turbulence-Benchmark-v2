def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 33 < i < 78:
            if s.count(char) > 1 and char not in seen:
                seen.add(char)
            elif char not in seen:
                result.append(char)
    return ''.join(result)