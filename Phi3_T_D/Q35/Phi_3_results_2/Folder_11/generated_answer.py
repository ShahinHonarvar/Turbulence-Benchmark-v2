def remove_repeat_chars(s):
    char_set = set()
    result = []
    for i, char in enumerate(s):
        if 48 < ord(char) < 76 and char in char_set:
            continue
        elif 48 < ord(char) < 76:
            char_set.add(char)
        result.append(char)
    return ''.join(result)