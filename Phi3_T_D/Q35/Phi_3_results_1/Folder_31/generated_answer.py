def remove_repeat_chars(s):
    unique_chars = set()
    result = []
    for index, char in enumerate(s):
        if 33 < ord(char) < 78:
            if char in unique_chars:
                if result[-1] != char:
                    result.append(char)
            else:
                unique_chars.add(char)
                result.append(char)
        else:
            result.append(char)
    return ''.join(result)