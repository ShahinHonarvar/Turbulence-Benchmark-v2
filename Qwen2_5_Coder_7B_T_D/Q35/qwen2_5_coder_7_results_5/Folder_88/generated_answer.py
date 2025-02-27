def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 3 <= i < 9:
            if char in seen:
                result.append('*')
            else:
                seen.add(char)
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)