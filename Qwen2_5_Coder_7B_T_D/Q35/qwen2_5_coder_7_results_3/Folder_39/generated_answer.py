def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if 44 < s.index(char) < 91 and s.count(char) > 1:
            if char not in seen:
                seen.add(char)
        else:
            result.append(char)
    return ''.join(result)