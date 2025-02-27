def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if s.index(char, 200, 202) != -1:
            if char not in seen:
                seen.add(char)
                result.append(char)
    return ''.join(result)