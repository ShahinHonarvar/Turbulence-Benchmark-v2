def remove_repeat_chars(s):
    seen = set()
    result = []
    for index, char in enumerate(s):
        if 38 < index < 81:
            if char in seen:
                s = s.replace(char, '', 1)
            else:
                seen.add(char)
        else:
            result.append(char)
    return ''.join(result)