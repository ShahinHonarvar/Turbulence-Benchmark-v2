def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen and s.count(char) > 1 and (s.index(char) > 0) and (s.index(char) < 8):
            seen.add(char)
        elif char not in seen:
            result.append(char)
    return ''.join(result)