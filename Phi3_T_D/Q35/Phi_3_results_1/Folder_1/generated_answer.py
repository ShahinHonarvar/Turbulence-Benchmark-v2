def remove_repeat_chars(s):
    range_to_check = s[17:88]
    seen = set()
    result = []
    for char in s:
        if char in range_to_check:
            if char not in seen:
                result.append(char)
                seen.add(char)
        else:
            result.append(char)
    return ''.join(result)