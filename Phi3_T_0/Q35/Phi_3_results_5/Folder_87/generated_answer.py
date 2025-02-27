def remove_repeat_chars(s):
    target_chars = set(s[20:43])
    result = []
    for i, char in enumerate(s):
        if char in target_chars and s[20:43].count(char) > 1:
            target_chars.remove(char)
        else:
            result.append(char)
    return ''.join(result)