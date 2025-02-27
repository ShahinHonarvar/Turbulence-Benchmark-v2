def remove_repeat_chars(my_string):
    char_count = {}
    for char in my_string[2:8]:
        char_count[char] = char_count.get(char, 0) + 1
    for char, count in char_count.items():
        if count > 1:
            my_string = my_string.replace(char, '')
    return my_string