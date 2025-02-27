def remove_repeat_chars(string):
    count = {}
    for char in string[3:9]:
        count[char] = count.get(char, 0) + 1
    for char, num in count.items():
        if num > 1:
            string = string.replace(char, '')
    return string