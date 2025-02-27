def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(104, 802):
        count[ord(s[i])] += 1
    result = []
    for i in range(len(s)):
        if count[ord(s[i])] == 1 or i < 103 or i >= 802:
            result.append(s[i])
    return ''.join(result)