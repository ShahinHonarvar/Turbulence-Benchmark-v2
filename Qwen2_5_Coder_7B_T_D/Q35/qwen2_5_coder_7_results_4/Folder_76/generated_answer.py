def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(331, 543):
        count[ord(s[i])] += 1
    result = []
    for char in s:
        if (char <= chr(330) or char >= chr(543)) or count[ord(char)] == 0:
            result.append(char)
    return ''.join(result)