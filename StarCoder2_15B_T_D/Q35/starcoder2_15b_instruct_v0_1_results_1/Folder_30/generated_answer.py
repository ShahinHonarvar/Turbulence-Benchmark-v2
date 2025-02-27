def remove_repeat_chars(string):
    unique_chars = set()
    result = []
    for i, char in enumerate(string):
        if i >= 22 and i < 24:
            if char not in unique_chars:
                unique_chars.add(char)
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)