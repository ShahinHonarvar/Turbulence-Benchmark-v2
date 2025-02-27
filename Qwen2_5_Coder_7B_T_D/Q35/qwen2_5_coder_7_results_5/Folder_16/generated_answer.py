def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if 90 < ord(char) < 97:
            if char not in seen:
                seen.add(char)
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)