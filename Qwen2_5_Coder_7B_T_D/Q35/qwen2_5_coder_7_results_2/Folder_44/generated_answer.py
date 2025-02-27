def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(36, 52):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if count[ord(char)] == 0 or (36 <= ord(char) < 52 and count[ord(char)] == 1):
            result.append(char)
    return ''.join(result)