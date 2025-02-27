def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if s.index(char) > 0 and s.index(char) < 7:
            if char not in seen:
                seen.add(char)
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)