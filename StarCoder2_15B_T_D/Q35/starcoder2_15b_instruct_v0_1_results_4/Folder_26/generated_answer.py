def remove_repeat_chars(string):
    counter = {}
    for char in string:
        counter[char] = counter.get(char, 0) + 1
    for char in counter:
        if counter[char] > 1:
            string = string.replace(char, '')
    return string