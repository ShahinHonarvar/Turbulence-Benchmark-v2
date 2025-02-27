def remove_repeat_chars(s):
    count = [0] * 256
    for char in s[27:96]:
        count[ord(char)] += 1
    result = []
    for char in s:
        if count[ord(char)] == 0:
            result.append(char)
    return ''.join(result)