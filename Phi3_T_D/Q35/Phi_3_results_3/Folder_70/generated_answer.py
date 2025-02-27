def remove_repeat_chars(input_string):
    start, end = (43, 70)
    charset = {}
    for i in range(start, end):
        char = input_string[i]
        if char in charset:
            charset[char] += 1
        else:
            charset[char] = 1
    output_list = [char for char in input_string if char not in charset or charset[char] == 1]
    return ''.join(output_list)