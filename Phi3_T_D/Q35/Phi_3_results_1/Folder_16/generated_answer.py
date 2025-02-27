def remove_repeat_chars(s):
    target_chars = set(s[91:97])
    result = []
    for char in s:
        if char in target_chars and s.count(char) > 1:
            if result.count(char) == 0:
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)