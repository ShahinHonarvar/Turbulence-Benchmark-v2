def remove_repeat_chars(s):
    counts = [0] * 256
    for i in range(477, 709):
        counts[ord(s[i])] += 1
    result = []
    for char in s:
        if counts[ord(char)] < 2:
            result.append(char)
    return ''.join(result)