def remove_repeat_chars(s):
    unique_chars = set()
    result = []
    for index, char in enumerate(s):
        if 29 < index < 53:
            if char in unique_chars:
                continue
            elif s.count(char) > 1:
                unique_chars.add(char)
        else:
            result.append(char)
    return ''.join(result)