def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(375, 926):
        count[ord(s[i])] += 1
    res = []
    for i in range(len(s)):
        if s[i] not in (c for c in s[375:926] if count[ord(c)] > 1):
            res.append(s[i])
    return ''.join(res)