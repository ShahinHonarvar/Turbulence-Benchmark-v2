def remove_repeat_chars(s):
    unique_chars = set()
    result = []
    for index, char in enumerate(s):
        if 355 < index < 988:
            if char in unique_chars:
                continue
            else:
                unique_chars.add(char)
        result.append(char)
    return ''.join(result)