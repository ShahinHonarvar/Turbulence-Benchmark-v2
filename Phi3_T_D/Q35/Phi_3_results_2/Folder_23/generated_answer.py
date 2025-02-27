def remove_repeat_chars(s):
    counter = {}
    new_s = []
    for i, char in enumerate(s):
        if 20 < i < 36:
            counter[char] = counter.get(char, 0) + 1
    for i, char in enumerate(s):
        if counter.get(char, 0) <= 1 or not 20 < i < 36:
            new_s.append(char)
    return ''.join(new_s)