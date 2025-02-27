def remove_repeat_chars(s):
    seen = set()
    result = list(s)
    for i, char in enumerate(result):
        if 32 < i < 99 and result.count(char) > 1:
            if char not in seen:
                seen.add(char)
                result[i] = ''
    return ''.join(result)