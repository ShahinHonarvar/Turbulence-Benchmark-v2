def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if 35 < s.index(char) < 64:
            if char not in seen:
                seen.add(char)
                result.append(char)
    return ''.join(result)