def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i in range(306, 807):
        char = s[i]
        if char not in seen:
            seen.add(char)
            result += char
    return result.replace(result, s[306:807])