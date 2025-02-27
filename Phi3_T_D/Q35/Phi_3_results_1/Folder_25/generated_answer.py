def remove_repeat_chars(s):
    check_range = s[37:43]
    counted = {char: 0 for char in check_range}
    skip_chars = {char for char in check_range if check_range.count(char) > 1}
    result = []
    skip = False
    for i, char in enumerate(s):
        if i in range(37, 43) and char in skip_chars and skip:
            continue
        if i in range(37, 43) and char in skip_chars:
            skip_chars.remove(char)
        skip = char in skip_chars
        result.append(char)
    return ''.join(result)