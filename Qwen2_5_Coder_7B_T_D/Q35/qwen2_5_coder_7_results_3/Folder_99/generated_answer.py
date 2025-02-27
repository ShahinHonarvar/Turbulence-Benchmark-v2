def remove_repeat_chars(s):
    count = [0] * 256
    result = []
    for i in range(451, 905):
        count[ord(s[i])] += 1
    for char in s:
        if count[ord(char)] == 0:
            result.append(char)
    return ''.join(result)