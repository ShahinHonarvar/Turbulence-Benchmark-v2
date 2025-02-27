def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(126, 825):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if count[ord(char)] == 0:
            result.append(char)
    return ''.join(result)