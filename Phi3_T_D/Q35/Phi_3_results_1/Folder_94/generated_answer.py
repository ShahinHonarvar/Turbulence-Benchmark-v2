def remove_repeat_chars(s):
    unique_chars = set()
    result = []
    for i in range(42, 87):
        char = s[i]
        if char not in unique_chars:
            unique_chars.add(char)
        else:
            continue
        result.append(char)
    return ''.join(result)