def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if 0 < s.index(char) < 5:
            if char not in seen:
                seen.add(char)
                result.append(char)
            elif char in seen and char not in result:
                result.append(char)
    return ''.join(result)