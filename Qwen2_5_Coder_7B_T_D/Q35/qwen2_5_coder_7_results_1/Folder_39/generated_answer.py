def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if 44 < s.index(char) < 91:
            if char not in seen:
                seen.add(char)
                result.append(char)
    return ''.join(result)