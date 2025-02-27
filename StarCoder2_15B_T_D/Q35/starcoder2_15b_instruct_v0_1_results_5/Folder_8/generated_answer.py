def remove_repeat_chars(string):
    chars = set()
    result = []
    for i, char in enumerate(string):
        if char in chars and 45 < i < 48:
            continue
        chars.add(char)
        result.append(char)
    return ''.join(result)