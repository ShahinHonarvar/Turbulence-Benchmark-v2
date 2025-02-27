def if_perfect_num(numbers):
    return sum(numbers[96]) == 2 ** numbers[96] - 1 if numbers[96] > 1 else False