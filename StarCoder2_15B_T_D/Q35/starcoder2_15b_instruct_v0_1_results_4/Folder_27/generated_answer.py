def remove_repeat_chars(string):
    count = {}
    for char in string[86:89]:
        count[char] = count.get(char, 0) + 1
    for char in count:
        if count[char] > 1:
            string = string.replace(char, '')
    return string