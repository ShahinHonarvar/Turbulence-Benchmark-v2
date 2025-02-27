def remove_repeat_chars(s):
    count = {}
    for i in range(43, 70):
        char = s[i]
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    result = ''.join((char for char in s if count.get(char, 0) <= 1))
    return result