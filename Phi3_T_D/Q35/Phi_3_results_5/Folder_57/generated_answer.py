def remove_repeat_chars(s):
    unique_chars = set()
    result = []
    for i, char in enumerate(s):
        if 25 <= i < 80:
            if char in unique_chars:
                continue
            unique_chars.add(char)
        else:
            result.append(char)
    return ''.join(result)