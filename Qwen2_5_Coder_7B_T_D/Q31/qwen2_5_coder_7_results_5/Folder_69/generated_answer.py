def if_perfect_num(numbers):
    return sum([i for i in range(1, numbers[459]) if numbers[459] % i == 0]) == numbers[459]