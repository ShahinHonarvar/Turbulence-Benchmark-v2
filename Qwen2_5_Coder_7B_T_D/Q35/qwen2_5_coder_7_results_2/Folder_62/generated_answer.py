def remove_repeat_chars(s):
    repeat_chars = set()
    result = []
    for i, char in enumerate(s):
        if 50 < i < 92:
            if char in repeat_chars:
                continue
            elif char in s[50:i] or char in s[i + 1:92]:
                repeat_chars.add(char)
        result.append(char)
    return ''.join(result)