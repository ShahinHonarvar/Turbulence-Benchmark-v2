def remove_repeat_chars(s):
    char_limit = [73, 84]
    char_count = {}
    result = []
    for i, char in enumerate(s):
        if char_limit[0] <= i < char_limit[1]:
            if char in char_count:
                char_count[char] += 1
                if char_count[char] == 1:
                    del char_count[char]
            else:
                char_count[char] = 1
    for i, char in enumerate(s):
        if char_limit[0] <= i < char_limit[1] or char_count.get(char) == 0:
            result.append(char)
    return ''.join(result)