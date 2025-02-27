def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(55, 84):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if count[ord(char)] == 0 or (55 <= ord(char) < 84 and count[ord(char)] == 1):
            result.append(char)
    return ''.join(result)