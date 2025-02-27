def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if 32 < s.index(char) < 44:
            if char not in seen:
                seen.add(char)
                result.append(char)
            else:
                result.append('')
        else:
            result.append(char)
    return ''.join(result)