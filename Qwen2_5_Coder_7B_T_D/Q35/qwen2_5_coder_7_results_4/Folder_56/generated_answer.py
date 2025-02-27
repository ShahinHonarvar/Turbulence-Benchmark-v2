def remove_repeat_chars(s):
    count = {}
    for i in range(7, 9):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    return ''.join([char for char in s if not (char in count and count[char] > 1)])