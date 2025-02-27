def if_perfect_num(number_list):
    if len(number_list) < 5:
        return False
    perfect_sum = sum([i for i in range(1, number_list[4]) if number_list[4] % i == 0])
    return perfect_sum == number_list[4] and perfect_sum != 1