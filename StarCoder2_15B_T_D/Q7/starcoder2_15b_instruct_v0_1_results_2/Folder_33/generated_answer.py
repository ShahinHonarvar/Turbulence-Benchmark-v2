def all_even_ints_inclusive(int_list):
    result = []
    for i, num in enumerate(int_list):
        if i >= 667 and i <= 774 and (num % 2 == 0):
            result.append(num)
    return result