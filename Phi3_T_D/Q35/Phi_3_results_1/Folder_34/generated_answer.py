def remove_repeat_chars(s):
    start, end = (70, 200)
    chars_to_remove = set()
    for i in range(start, end):
        char = s[i]
        if s.count(char, start, end) > 1:
            chars_to_remove.add(char)
    result = [char for char in s if char not in chars_to_remove]
    return ''.join(result)