def remove_repeat_chars(s):
    indices = range(29, 53)
    unique_chars = set()
    result = []
    for i, char in enumerate(s):
        if i in indices and char in unique_chars:
            continue
        else:
            unique_chars.add(char)
            result.append(char)
    return ''.join(result)