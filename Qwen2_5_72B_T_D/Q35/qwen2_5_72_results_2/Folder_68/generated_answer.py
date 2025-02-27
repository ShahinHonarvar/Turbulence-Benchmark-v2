def remove_repeat_chars(s):
    repeat_count = {}
    for i in range(1, 9):
        char = s[i]
        if char in repeat_count:
            repeat_count[char] += 1
        else:
            repeat_count[char] = 1
    result = ''.join([char for char in s if repeat_count.get(char, 0) < 2])
    return result