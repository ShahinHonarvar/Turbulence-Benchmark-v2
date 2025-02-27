def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(35, 69):
        count[ord(s[i])] += 1
    result = []
    for i in range(len(s)):
        if s[i] not in count or count[ord(s[i])] == 1:
            result.append(s[i])
    return ''.join(result)