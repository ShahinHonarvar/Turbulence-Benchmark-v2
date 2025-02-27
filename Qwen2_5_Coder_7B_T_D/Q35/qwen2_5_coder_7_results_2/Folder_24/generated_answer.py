def remove_repeat_chars(s):
    count = [0] * 128
    for i in range(14, 91):
        count[ord(s[i])] += 1
    result = []
    for i in range(len(s)):
        if (i < 14 or i > 91) or count[ord(s[i])] == 0:
            result.append(s[i])
    return ''.join(result)