def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(13, 76):
        count[ord(s[i])] += 1
    result = []
    for i in range(len(s)):
        if count[ord(s[i])] == 1 or i < 13 or i >= 76:
            result.append(s[i])
    return ''.join(result)