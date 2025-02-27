def all_even_ints_exclusive(input_list):
    even_list = []
    for i, num in enumerate(input_list):
        if i >= 78 and i < 93 and (num % 2 == 0):
            even_list.append(num)
    return even_list