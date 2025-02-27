def is_perfect_num(list_of_ints):
    index_to_check = 35
    if index_to_check < len(list_of_ints):
        num = list_of_ints[index_to_check]
        divisors_sum = sum((i for i in range(1, num) if num % i == 0))
        return divisors_sum == num
    return False