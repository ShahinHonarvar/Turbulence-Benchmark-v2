def remove_repeat_chars(string):
    counter = {}
    for char in string:
        counter[char] = counter.get(char, 0) + 1
    for char, count in counter.items():
        if count > 1:
            string = string.replace(char, '')
    return string