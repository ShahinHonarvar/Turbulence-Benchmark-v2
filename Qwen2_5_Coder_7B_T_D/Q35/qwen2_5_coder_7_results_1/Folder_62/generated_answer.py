def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if 50 < s.index(char) < 92:
            if char not in seen:
                seen.add(char)
                result.append(char)
    return ''.join(result)