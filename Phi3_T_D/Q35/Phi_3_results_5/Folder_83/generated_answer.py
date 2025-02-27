def remove_repeat_chars(input_string):
    start, end = (100, 200)
    counts = {}
    new_string = list(input_string)
    for i, char in enumerate(input_string[start:end]):
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for i in range(start, end):
        if counts[input_string[i]] > 1:
            new_string[i] = ''
    return ''.join(new_string)