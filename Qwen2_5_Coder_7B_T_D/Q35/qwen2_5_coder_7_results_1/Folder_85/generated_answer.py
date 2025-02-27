def remove_repeat_chars(s):
    temp = s[0] + s[8:]
    result = [temp[0]]
    for char in temp[1:]:
        if char not in result:
            result.append(char)
    return ''.join(result)