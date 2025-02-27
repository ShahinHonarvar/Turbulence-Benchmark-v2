def remove_repeat_chars(s):
    char_count = {}
    for i in range(48, 76):
        char_count[chr(i)] = s.count(chr(i))
    to_remove = {char for char, count in char_count.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))