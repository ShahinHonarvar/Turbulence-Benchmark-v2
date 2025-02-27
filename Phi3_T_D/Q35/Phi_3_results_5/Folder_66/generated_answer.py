def remove_repeat_chars(s):
    start, end = (11, 76)
    char_indices = {}
    for index in range(start, end):
        char = s[index]
        if char in char_indices and char_indices[char] < start:
            while char in s[start:end]:
                s = s.replace(char, '', 1)
        else:
            char_indices[char] = index
    return s