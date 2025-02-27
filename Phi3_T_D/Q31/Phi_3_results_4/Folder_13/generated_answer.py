def if_perfect_num(number_list):
    if len(number_list) > 126:
        perfect_sum = sum((i for i in range(1, number_list[126]) if number_list[126] % i == 0))
        return perfect_sum == number_list[126]
    return False