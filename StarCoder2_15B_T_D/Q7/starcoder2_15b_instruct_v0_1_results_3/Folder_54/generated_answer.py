def all_even_ints_inclusive(my_list):
    result = []
    for index, num in enumerate(my_list):
        if index >= 34 and index <= 55 and (num % 2 == 0):
            result.append(num)
    return result