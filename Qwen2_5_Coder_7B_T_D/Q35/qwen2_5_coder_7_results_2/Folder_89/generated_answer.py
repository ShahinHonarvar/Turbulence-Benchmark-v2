def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(55, 84):
        count[ord(s[i])] += 1
    result = []
    for i in range(len(s)):
        if count[ord(s[i])] == 1 or i < 55 or i >= 84:
            result.append(s[i])
    return ''.join(result)