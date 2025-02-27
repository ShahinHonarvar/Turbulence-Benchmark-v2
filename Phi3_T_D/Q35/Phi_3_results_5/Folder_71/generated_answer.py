def remove_repeat_chars(input_string):
    count = {}
    for i in range(20, 34):
        if input_string[i] in count:
            count[input_string[i]] += 1
        else:
            count[input_string[i]] = 1
    to_remove = [char for char, freq in count.items() if freq > 1]
    return ''.join([char for char in input_string if char not in to_remove])