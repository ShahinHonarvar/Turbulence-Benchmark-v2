def remove_repeat_chars(input_string):
    count = {}
    for i in range(30, 200):
        if input_string[i] in count:
            count[input_string[i]] += 1
        else:
            count[input_string[i]] = 1
    result = []
    for char in input_string:
        if char not in count or count[char] == 1:
            result.append(char)
    return ''.join(result)