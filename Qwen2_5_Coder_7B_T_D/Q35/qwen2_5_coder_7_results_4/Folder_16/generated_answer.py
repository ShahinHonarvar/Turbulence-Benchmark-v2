def remove_repeat_chars(s):
    seen = set()
    result = []
    for char in s:
        if ord(char) in range(91, 97):
            if char not in seen:
                seen.add(char)
                result.append(char)
            else:
                result.append('')
        else:
            result.append(char)
    return ''.join(result)