def remove_repeat_chars(s):
    count = [0] * 256
    for i in range(104, 802):
        count[ord(s[i])] += 1
    result = []
    for i in range(len(s)):
        if i < 104 or i > 801 or count[ord(s[i])] == 1:
            result.append(s[i])
    return ''.join(result)