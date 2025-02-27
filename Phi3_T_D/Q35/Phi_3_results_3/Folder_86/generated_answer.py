def remove_repeat_chars(s):
    chars_to_remove = set()
    initial_string = list(s)
    for i in range(19, 32):
        if s.count(s[i]) > 1:
            chars_to_remove.add(s[i])
    altered_string = [char for char in initial_string if char not in chars_to_remove]
    return ''.join(altered_string)