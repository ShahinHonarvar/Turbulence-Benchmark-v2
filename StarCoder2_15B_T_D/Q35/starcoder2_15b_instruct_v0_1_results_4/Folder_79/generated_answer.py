def remove_repeat_chars(s):
    count = [0] * 256
    for c in s:
        count[ord(c)] += 1
    result = []
    for c in s:
        if count[ord(c)] > 1 and 1 < ord(c) < 7:
            count[ord(c)] = 0
        else:
            result.append(c)
    return ''.join(result)