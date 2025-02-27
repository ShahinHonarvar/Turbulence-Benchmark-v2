def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if s.index(char) > 0 and s.index(char) < 7 and (char in seen):
            continue
        if s.count(char, 1, 7) > 0:
            seen.add(char)
        result.append(char)
    return ''.join(result)