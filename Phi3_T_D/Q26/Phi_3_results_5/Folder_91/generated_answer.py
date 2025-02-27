def sum_in_range(number_list):
    total = sum((num for num in number_list if -8 <= num <= 8))
    return total