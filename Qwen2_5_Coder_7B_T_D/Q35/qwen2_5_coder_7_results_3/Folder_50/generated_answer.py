def remove_repeat_chars(s):
    count = [0] * 256
    result = []
    for char in s:
        if 13 < ord(char) < 76:
            count[ord(char)] += 1
    for char in s:
        if count[ord(char)] == 1 or not 13 < ord(char) < 76:
            result.append(char)
    return ''.join(result)