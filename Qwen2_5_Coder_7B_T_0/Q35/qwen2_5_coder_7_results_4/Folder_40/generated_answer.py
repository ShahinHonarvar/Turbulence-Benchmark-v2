def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if s.index(char) > 0 and s.index(char) < 3 and (char in seen):
            continue
        if s.index(char) > 0 and s.index(char) < 3:
            seen.add(char)
        result.append(char)
    return ''.join(result)