def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, char in enumerate(s):
        if 45 < i < 48:
            if char not in seen:
                seen.add(char)
                result += char
            elif char in seen:
                result += char
        else:
            result += char
    return result