def remove_repeat_chars(s):
    chars_to_remove = []
    index_range = range(32, 44)
    for index in index_range:
        char = s[index]
        if s.count(char) > 1:
            chars_to_remove.append(char)
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result