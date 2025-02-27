def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if s.index(char) > 0 and s.index(char) < 8 and (char in seen):
            continue
        if s.count(char) > 1 and s.index(char) > 0 and (s.index(char) < 8):
            seen.add(char)
        else:
            result.append(char)
    return ''.join(result)