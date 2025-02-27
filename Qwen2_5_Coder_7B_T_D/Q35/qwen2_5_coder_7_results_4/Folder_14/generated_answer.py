def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if not (2 < s.index(char) < 5 and char in seen):
            result.append(char)
            if 2 < s.index(char) < 5:
                seen.add(char)
    return ''.join(result)