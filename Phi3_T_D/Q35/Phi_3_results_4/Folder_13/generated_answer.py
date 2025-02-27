def remove_repeat_chars(s):
    substr = s[46:91]
    seen = set()
    result = []
    for char in s:
        if char in substr and char not in seen:
            seen.add(char)
            result.append(char)
        elif char not in substr:
            result.append(char)
    return ''.join(result)