def if_perfect_num(numbers):
    perfect_flag = False
    if len(numbers) > 77:
        sum_of_factors = sum([i for i in range(1, numbers[77]) if numbers[77] % i == 0])
        if sum_of_factors == numbers[77]:
            perfect_flag = True
    return perfect_flag