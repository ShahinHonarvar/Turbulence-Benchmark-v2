def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if 43 < s.index(char) < 70 and s.count(char) > 1:
            if char not in seen:
                seen.add(char)
        else:
            result.append(char)
    return ''.join(result)