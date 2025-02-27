def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(57, 90):
        count[ord(s[i])] += 1
    res = []
    for i in range(len(s)):
        if count[ord(s[i])] == 1 or i < 56 or i >= 90:
            res.append(s[i])
    return ''.join(res)