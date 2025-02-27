def remove_repeat_chars(s):
    chars_to_remove = set(s[13:91])
    result = []
    for idx, char in enumerate(s):
        if idx >= 13 and idx <= 90 and (char in chars_to_remove):
            continue
        else:
            result.append(char)
    return ''.join(result)