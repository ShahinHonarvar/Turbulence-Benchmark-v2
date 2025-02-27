def remove_repeat_chars(s):
    target_chars = set(s[36:54])
    result = []
    for char in s:
        if char in target_chars and s[36:54].count(char) > 1:
            target_chars.remove(char)
        else:
            result.append(char)
    return ''.join(result)