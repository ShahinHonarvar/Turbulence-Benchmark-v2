def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if 1 < s.index(char) < 7 and s.count(char) > 1 and (char not in seen):
            seen.add(char)
        elif char not in seen:
            result.append(char)
    return ''.join(result)