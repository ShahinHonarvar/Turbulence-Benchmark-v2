def remove_repeat_chars(s):
    repeat_chars = set()
    result = []
    for i, char in enumerate(s):
        if 86 < i < 89:
            if char in repeat_chars:
                continue
            elif char in s[86:89]:
                repeat_chars.add(char)
        result.append(char)
    return ''.join(result)